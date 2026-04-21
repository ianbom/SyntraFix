# Alur Ingestion Dokumen Syntra

Dokumen ini menjelaskan alur ingestion dokumen Syntra secara lengkap: mulai dari user meng-upload PDF, file disimpan, task dikirim ke Celery melalui RabbitMQ, worker memproses dokumen, sampai chunk dan embedding tersimpan di database.

Fokus utama dokumen ini:

- alur ingestion dokumen secara runtut
- flow diagram ingestion
- peran FastAPI, Celery, RabbitMQ, MinIO, GROBID, PyMuPDF, Ollama/LLM, dan database
- bagaimana Celery dan RabbitMQ bekerja di Syntra
- apa yang terjadi ketika worker lebih dari satu
- bagaimana status processing dokumen diperbarui

## Gambaran Singkat

Ingestion dokumen di Syntra tidak dikerjakan langsung oleh endpoint upload. Endpoint upload hanya melakukan pekerjaan cepat:

1. validasi file PDF
2. upload PDF ke MinIO
3. membuat record `Document` di database dengan status `processing`
4. mengirim task ke Celery
5. langsung mengembalikan response ke frontend

Pekerjaan berat seperti ekstraksi PDF, chunking, question generation, embedding, dan penyimpanan chunk dikerjakan di background oleh Celery worker.

Alur sederhananya:

```text
User Upload PDF
-> FastAPI menerima file
-> PDF disimpan ke MinIO
-> Document dibuat di database
-> FastAPI mengirim task ke RabbitMQ
-> Celery worker mengambil task
-> Worker memproses PDF
-> Worker menyimpan metadata, chunk, questions, embedding
-> Document ditandai completed atau failed
```

## Komponen yang Terlibat

| Komponen | Peran |
| --- | --- |
| FastAPI | Menerima upload dari user dan mengirim task background |
| RabbitMQ | Broker/antrian task antara FastAPI dan Celery worker |
| Celery | Sistem background job yang menjalankan task ingestion |
| Celery worker | Proses yang mengambil task dari RabbitMQ dan menjalankan `process_document_task` |
| MinIO | Object storage untuk menyimpan file PDF asli |
| PostgreSQL | Menyimpan metadata dokumen, chunk, embedding, chat reference, dan status |
| GROBID | Mengekstrak metadata akademik, fulltext, references, dan structured sections |
| PyMuPDF | Mengekstrak teks halaman, tabel, dan gambar dari PDF |
| LLM | Fallback metadata, deskripsi tabel/gambar, dan question generation |
| Ollama embedding model | Membuat vector embedding untuk content dan possibly questions |

## Flow Diagram Utama

```mermaid
flowchart TD
    A["User upload PDF"] --> B["FastAPI POST /documents/upload"]
    B --> C["Validasi file PDF dan ukuran"]
    C --> D["Upload PDF ke MinIO"]
    D --> E["Create Document di PostgreSQL<br/>status=processing, progress=0"]
    E --> F["process_document_task.delay(document_id, file_path)"]
    F --> G["RabbitMQ menerima task message"]
    G --> H["Celery worker mengambil task"]
    H --> I["Download PDF dari MinIO"]
    I --> J["GROBID extraction<br/>header, references, fulltext, structured sections"]
    J --> K["PyMuPDF extraction<br/>raw text, page data, tables, images"]
    K --> L["Metadata fallback dengan LLM jika perlu"]
    L --> M["Update metadata Document"]
    M --> N{"Structured sections tersedia?"}
    N -->|Ya| O["SmartChunker"]
    N -->|Tidak| P["Legacy TextChunker"]
    P --> Q["Tambah title chunk dan abstract chunk jika tersedia"]
    O --> R["Attach context metadata<br/>document title, section, page"]
    Q --> R
    R --> S["Build table chunks dan image chunks"]
    S --> T["Generate possibly_questions"]
    T --> U["Generate possibly_question_embedding"]
    U --> V["Build embedding_text"]
    V --> W["Generate content embedding"]
    W --> X["Save DocumentChunk ke PostgreSQL"]
    X --> Y["Set Document completed, progress=100"]

    H --> Z["Jika error"]
    Z --> AA["Set Document failed atau retry task"]
```

## Flow Diagram Celery dan RabbitMQ

```mermaid
sequenceDiagram
    participant User
    participant FastAPI
    participant DB as PostgreSQL
    participant MinIO
    participant RabbitMQ
    participant Worker as Celery Worker

    User->>FastAPI: Upload PDF
    FastAPI->>FastAPI: Validasi file
    FastAPI->>MinIO: Upload PDF
    MinIO-->>FastAPI: file_path
    FastAPI->>DB: Insert Document(status=processing)
    DB-->>FastAPI: document_id
    FastAPI->>RabbitMQ: Publish task process_document_task(document_id, file_path)
    FastAPI-->>User: Response cepat, processing

    RabbitMQ-->>Worker: Deliver task
    Worker->>DB: Set progress=0, clear error
    Worker->>MinIO: Download PDF
    Worker->>DB: Update progress=10
    Worker->>Worker: Extract, chunk, questions, embeddings
    Worker->>DB: Save metadata dan chunks
    Worker->>DB: Set status=completed, progress=100
    Worker-->>RabbitMQ: ACK task selesai
```

## Tahap 1: Upload Masuk ke FastAPI

Endpoint utama:

```text
POST /documents/upload
```

File terkait:

```text
app/api/routes/documents.py
```

Fungsi utama:

```python
upload_document(...)
```

Endpoint menerima:

- file PDF
- `type`
- `is_private`
- optional `client_id`
- database session

Pada tahap ini, FastAPI masih berada di request-response lifecycle. Artinya user masih menunggu response HTTP.

Karena itu, endpoint upload tidak boleh menjalankan pemrosesan PDF yang berat secara langsung. Jika ekstraksi PDF, chunking, dan embedding dijalankan langsung di endpoint, user harus menunggu lama dan request berisiko timeout.

## Tahap 2: Validasi PDF

FastAPI menjalankan validasi:

```python
FileValidator.validate_pdf(file)
file_content = await file.read()
FileValidator.validate_size(file_content)
```

Validasi ini memastikan:

- file adalah PDF
- ukuran file masih masuk batas
- file tidak kosong atau invalid

Jika validasi gagal, endpoint mengembalikan error dan tidak ada task Celery yang dikirim.

## Tahap 3: Upload File ke MinIO

Setelah valid, file disimpan ke MinIO:

```python
storage = MinIOStorage()
file_path = storage.upload_file(file_content, file.filename)
```

Kenapa PDF disimpan ke MinIO?

- database tidak perlu menyimpan binary PDF besar
- worker Celery bisa mengambil file menggunakan `file_path`
- file asli tetap tersedia untuk download/detail dokumen
- proses upload dan proses ingestion bisa dipisah

Output tahap ini adalah:

```text
file_path
```

`file_path` inilah yang dikirim ke task Celery.

## Tahap 4: Membuat Record Document Awal

FastAPI membuat record awal di tabel `documents`:

```python
document = Document(
    title="Sedang diproses...",
    file_path=file_path,
    type=doc_type,
    is_private=is_private,
    format="application/pdf",
    processing_status="processing",
    processing_progress=0,
)
```

Record ini penting karena:

- frontend langsung mendapat `document_id`
- status dokumen bisa dipantau
- Celery worker tahu dokumen mana yang harus diperbarui
- jika task gagal, error bisa disimpan ke document yang sama

Setelah commit, FastAPI memiliki:

```text
document.id
file_path
```

## Tahap 5: FastAPI Mengirim Task ke Celery

FastAPI menjalankan:

```python
process_document_task.delay(document.id, file_path)
```

Ini bukan menjalankan fungsi secara langsung.

Yang terjadi sebenarnya:

1. Celery membuat message berisi nama task dan argumen.
2. Message dikirim ke RabbitMQ.
3. RabbitMQ menyimpan message di queue.
4. Worker yang sedang aktif akan mengambil message tersebut.

Argumen task:

```text
document_id
file_path
```

Dengan demikian, FastAPI tidak membawa file PDF ke worker secara langsung. Worker mengambil ulang PDF dari MinIO berdasarkan `file_path`.

## Tahap 6: Response Cepat ke Frontend

Setelah task berhasil dikirim ke RabbitMQ, endpoint upload langsung mengembalikan response:

```python
return build_document_response(document, 0)
```

Frontend akan melihat dokumen dengan status:

```text
processing
```

Frontend bisa memantau status melalui:

```text
GET /documents/{document_id}/status
```

Atau melalui WebSocket jika `client_id` digunakan.

## Apa Itu Celery?

Celery adalah sistem background task/job queue untuk Python.

Dalam Syntra, Celery dipakai agar pekerjaan berat tidak mengunci request FastAPI.

Tanpa Celery:

```text
User upload PDF
-> FastAPI ekstrak PDF
-> FastAPI chunking
-> FastAPI generate questions
-> FastAPI generate embeddings
-> User menunggu lama
```

Dengan Celery:

```text
User upload PDF
-> FastAPI simpan file dan kirim task
-> User langsung menerima response
-> Worker memproses dokumen di background
```

Celery memiliki tiga konsep utama:

| Konsep | Penjelasan |
| --- | --- |
| Producer | Aplikasi yang mengirim task. Di Syntra: FastAPI |
| Broker | Antrian task. Di Syntra: RabbitMQ |
| Consumer/Worker | Proses yang mengambil dan menjalankan task. Di Syntra: Celery worker |

## Apa Itu RabbitMQ?

RabbitMQ adalah message broker.

Broker berarti perantara antara pengirim task dan pemroses task.

Dalam Syntra:

```text
FastAPI tidak langsung memanggil Celery worker.
FastAPI mengirim pesan ke RabbitMQ.
Celery worker mengambil pesan dari RabbitMQ.
```

RabbitMQ menyimpan task dalam queue sampai ada worker yang mengambilnya.

Ini membuat sistem lebih tahan terhadap kondisi seperti:

- worker sedang sibuk
- banyak dokumen di-upload bersamaan
- worker baru dinyalakan setelah task masuk
- worker lebih dari satu

## Konfigurasi Celery di Syntra

File konfigurasi:

```text
app/celery_app.py
```

Konfigurasi utama:

```python
celery_app = Celery(
    "syntra_worker",
    broker=settings.CELERY_BROKER_URL,
    include=["app.tasks.document_tasks"]
)
```

Broker diambil dari:

```text
CELERY_BROKER_URL
```

Default di config:

```text
amqp://guest:guest@localhost:5672//
```

Artinya Celery memakai RabbitMQ melalui protokol AMQP.

## Konfigurasi Penting Celery

```python
worker_concurrency=2
worker_prefetch_multiplier=1
task_acks_late=True
task_reject_on_worker_lost=True
task_time_limit=600
task_soft_time_limit=540
```

### `worker_concurrency=2`

Secara konfigurasi default, worker dapat menjalankan 2 task paralel.

Namun jika worker dijalankan dengan command:

```bash
celery -A app.celery_app worker --loglevel=info --pool=solo
```

maka `--pool=solo` membuat satu worker hanya menjalankan satu task pada satu waktu.

Untuk menambah paralelisme dengan `solo`, jalankan beberapa worker di terminal berbeda dengan hostname berbeda.

### `worker_prefetch_multiplier=1`

Ini sangat penting untuk ingestion dokumen.

Prefetch menentukan berapa banyak task yang boleh diambil worker dari RabbitMQ sebelum benar-benar selesai dikerjakan.

Dengan:

```text
worker_prefetch_multiplier=1
```

worker hanya mengambil task secukupnya. Ini mencegah satu worker mengambil terlalu banyak dokumen lalu menahan antrean, sementara worker lain menganggur.

Untuk task berat seperti ingestion PDF, nilai `1` adalah pilihan baik.

### `task_acks_late=True`

ACK berarti acknowledgement, yaitu tanda ke RabbitMQ bahwa task sudah selesai.

Dengan `acks_late=True`, Celery baru mengirim ACK setelah task selesai diproses.

Keuntungannya:

- jika worker mati di tengah proses, RabbitMQ tidak menganggap task sudah selesai
- task bisa dikirim ulang ke worker lain

Risikonya:

- task harus aman jika dijalankan ulang
- jika retry terjadi setelah sebagian data tersimpan, perlu hati-hati agar tidak ada duplicate chunk

### `task_reject_on_worker_lost=True`

Jika worker hilang atau crash, task ditolak dan bisa dikembalikan ke queue.

Ini membantu agar dokumen tidak berhenti menggantung hanya karena worker mati.

### `task_time_limit=600`

Hard time limit 600 detik, atau 10 menit.

Jika task lebih lama dari ini, Celery dapat menghentikan task.

### `task_soft_time_limit=540`

Soft time limit 540 detik, atau 9 menit.

Soft limit memberi kesempatan task menangani timeout sebelum dipaksa berhenti oleh hard limit.

Untuk dokumen besar, banyak gambar, atau embedding lambat, batas 9-10 menit bisa menjadi faktor penting.

## Cara Worker Mengambil Task dari RabbitMQ

Saat worker dijalankan:

```bash
celery -A app.celery_app worker --loglevel=info --pool=solo
```

Worker akan:

1. membaca konfigurasi `app.celery_app`
2. connect ke RabbitMQ dari `CELERY_BROKER_URL`
3. mendaftarkan task dari `include=["app.tasks.document_tasks"]`
4. subscribe ke queue default
5. menunggu message task

Ketika FastAPI mengirim:

```python
process_document_task.delay(document.id, file_path)
```

RabbitMQ menerima message dengan isi kira-kira:

```json
{
  "task": "process_document_task",
  "args": [123, "path/to/file.pdf"],
  "kwargs": {}
}
```

Worker mengambil message tersebut dan menjalankan:

```python
process_document_task(document_id=123, file_path="path/to/file.pdf")
```

## Apa yang Terjadi Jika Worker Lebih dari Satu?

Jika ada beberapa Celery worker yang terhubung ke RabbitMQ queue yang sama, RabbitMQ akan membagikan task ke worker yang tersedia.

Contoh:

```text
worker1 sedang memproses dokumen A
worker2 sedang idle
user upload dokumen B
RabbitMQ mengirim task dokumen B ke worker2
```

Dengan `--pool=solo`, setiap worker memproses satu task.

Jika menjalankan dua worker solo:

```text
worker1 -> 1 dokumen
worker2 -> 1 dokumen
```

Maka Syntra bisa memproses 2 dokumen bersamaan.

Contoh command:

```powershell
celery -A app.celery_app worker --loglevel=info --pool=solo --hostname=worker1@%h
celery -A app.celery_app worker --loglevel=info --pool=solo --hostname=worker2@%h
```

Worker pertama tidak perlu dihentikan. Worker kedua bisa dijalankan di terminal baru.

## Lifecycle Task Ingestion

Task utama:

```python
@shared_task(name="process_document_task", bind=True, max_retries=2)
def process_document_task(self, document_id: int, file_path: str):
```

Karena `bind=True`, task menerima `self`.

`self` digunakan untuk fitur Celery seperti:

```python
self.retry(...)
```

Karena `max_retries=2`, task bisa dicoba ulang maksimal 2 kali jika error yang dianggap transient terjadi.

## Progress Dokumen

Worker memperbarui status dokumen melalui helper:

```python
_update_processing_state(...)
```

Progress utama:

| Progress | Tahap |
| --- | --- |
| 0% | Task mulai, status processing |
| 10% | PDF berhasil di-download dari MinIO |
| 30% | Metadata dan struktur berhasil diekstrak dengan GROBID |
| 45% | Raw text, halaman, tabel, gambar berhasil diekstrak |
| 55% | Metadata document berhasil diperbarui |
| 65% | Chunk berhasil dibuat |
| 75% | Possibly questions selesai |
| 90% | Content embeddings selesai |
| 95% | Chunk sedang/sudah disimpan |
| 100% | Document completed |

Progress untuk question generation dan embedding dihitung bertahap berdasarkan jumlah chunk:

```python
_calculate_phase_progress(start_progress, end_progress, current_index, total_items)
```

Jadi jika dokumen punya banyak chunk, progress akan bergerak sedikit demi sedikit.

## Tahap Worker 1: Download PDF dari MinIO

Worker membuat object storage:

```python
storage = MinIOStorage()
```

Lalu download:

```python
file_content = storage.download_file(file_path)
```

Jika file tidak ditemukan di MinIO, task gagal karena tidak ada PDF yang bisa diproses.

## Tahap Worker 2: GROBID Extraction

Worker memanggil:

```python
header = _run_async(extract_header(file_content))
references = extract_references(file_content)
fulltext = extract_fulltext(file_content)
structured_sections = extract_structured_fulltext(file_content)
```

GROBID dipakai karena dokumen akademik memiliki struktur yang bisa dikenali:

- title
- authors
- abstract
- sections
- references
- citation metadata

Output GROBID diproses:

```python
metadata = format_for_database(header, references)
metadata["fulltext"] = fulltext or ""
metadata["structured_sections"] = structured_sections
```

Jika structured sections berhasil, Syntra bisa melakukan smart chunking.

## Tahap Worker 3: PyMuPDF Extraction

Worker juga mengekstrak PDF dengan PyMuPDF:

```python
raw_pdf_text, pages_data = extract_raw_pdf_text(file_content)
tables_data, images_data = extract_pdf_tables_and_images(file_content)
```

PyMuPDF membantu untuk:

- teks mentah per halaman
- mapping chunk ke halaman
- ekstraksi tabel
- ekstraksi gambar
- fallback jika GROBID kurang lengkap

GROBID dan PyMuPDF saling melengkapi.

## Tahap Worker 4: Metadata Fallback

Jika metadata masih belum lengkap:

```python
if is_metadata_incomplete(metadata):
    llm_metadata = _run_async(extract_metadata_with_llm(llm_input_text, metadata))
    metadata = merge_metadata(metadata, llm_metadata)
```

LLM dipakai sebagai fallback, bukan sumber utama.

Setelah itu metadata divalidasi:

```python
metadata = validate_metadata(metadata, raw_pdf_text or fulltext or "")
```

Lalu record `Document` diperbarui.

## Tahap Worker 5: Smart Chunking atau Legacy Chunking

Jika `structured_sections` tersedia:

```python
smart_chunker = SmartChunker()
chunks = smart_chunker.chunk_structured_sections(...)
```

Jika tidak tersedia:

```python
chunker = TextChunker()
chunks = chunker.chunk_text(...)
```

Fallback legacy juga dapat menambahkan:

- abstract chunk
- title chunk

Tujuan chunking:

- memecah dokumen panjang menjadi potongan yang bisa dicari
- menjaga konteks section
- membuat retrieval lebih presisi
- menjaga chunk tidak terlalu panjang untuk embedding dan prompt RAG

## Tahap Worker 6: Attach Context Metadata

Setiap chunk diberi metadata:

```python
chunk_metadata["source_document"] = document_title
chunk_metadata["section"] = section_title
chunk_metadata["page_number"] = page_number
chunk_metadata["context_in_metadata"] = True
```

Context tidak disisipkan ke `content`.

Alasannya:

- `content` tetap bersih untuk quote/reference
- konteks tetap tersedia untuk embedding
- debug lebih mudah

## Tahap Worker 7: Table dan Image Chunks

Worker membangun chunk tambahan:

```python
table_chunks = _build_table_chunks(tables_data, metadata.get("title"))
image_chunks = _build_image_chunks(images_data, metadata.get("title"))
chunks.extend(table_chunks)
chunks.extend(image_chunks)
```

Ini membuat informasi visual ikut masuk knowledge base.

Contoh:

- tabel hasil evaluasi model menjadi teks
- grafik performa model menjadi deskripsi teks
- figure arsitektur menjadi deskripsi teks

Catatan penting: chunk gambar/tabel bisa berisi deskripsi hasil LLM, jadi tidak selalu teks asli dari PDF.

## Tahap Worker 8: Generate Possibly Questions

Untuk setiap chunk:

```python
questions = _run_async(generate_possibly_questions(...))
```

Possibly questions adalah pertanyaan yang mungkin bisa dijawab oleh chunk.

Contoh:

```text
Apa fungsi CNN dalam dokumen Pengembangan Deteksi Kanker?
Bagaimana CNN digunakan pada bagian Metodologi?
```

Possibly questions membantu retrieval karena pertanyaan user sering tidak sama persis dengan teks chunk.

Jika question generation gagal dan `token_count >= 30`, fallback dipakai:

```python
possibly_questions = _build_fallback_questions(...)
```

Tujuannya agar chunk yang cukup panjang tidak masuk database dengan `possibly_questions = null`.

## Tahap Worker 9: Generate Possibly Question Embedding

Jika questions tersedia:

```python
combined_questions = " ".join(questions)
possibly_question_embedding = generate_embedding(combined_questions)
```

Embedding ini disimpan ke:

```text
DocumentChunk.possibly_question_embedding
```

Saat user chat, embedding ini menjadi jalur retrieval kedua selain content embedding.

## Tahap Worker 10: Build Embedding Text

Untuk content embedding, Syntra tidak hanya memakai `content`.

Syntra membuat:

```python
embedding_text = build_embedding_text(chunk_data)
```

Format:

```text
Judul Dokumen: <source_document>
Bagian: <section_title>
Subbagian: <sub_section>
Tipe Konten: <chunk_type>
Halaman: <page_number>

Konten:
<content>
```

Manfaat:

- embedding punya konteks judul dokumen
- section ikut mempengaruhi embedding
- chunk pendek lebih mudah ditemukan
- query yang menyebut judul dokumen lebih akurat

`embedding_text` juga disimpan ke:

```text
chunk_metadata["embedding_text"]
```

## Tahap Worker 11: Generate Content Embedding

Worker membuat embedding:

```python
chunk_data["_embedding"] = generate_embedding(embedding_text)
```

Service embedding mengirim request ke Ollama:

```text
POST <OLLAMA_BASE_URL>/api/embeddings
```

Payload berisi:

```json
{
  "model": "OLLAMA_EMBEDDING_MODEL",
  "prompt": "embedding_text",
  "output_dimensionality": "OLLAMA_EMBEDDING_DIMENSION"
}
```

Embedding harus sesuai dimensi config.

Jika config memakai BGE-M3 1024, database juga harus memakai:

```text
vector(1024)
```

Jika config memakai embeddinggemma 768, database harus memakai:

```text
vector(768)
```

## Tahap Worker 12: Simpan Chunk ke Database

Setiap chunk disimpan sebagai `DocumentChunk`:

```python
chunk = DocumentChunk(
    document_id=document.id,
    chunk_index=chunk_data["chunk_index"],
    content=chunk_data["content"],
    token_count=chunk_data.get("token_count", ...),
    embedding=chunk_data.get("_embedding"),
    chunk_type=chunk_data.get("chunk_type"),
    page_number=chunk_data.get("page_number"),
    section_title=chunk_data.get("section_title"),
    chunk_metadata=chunk_data.get("chunk_metadata"),
    possibly_questions=chunk_data.get("_possibly_questions"),
    possibly_question_embedding=chunk_data.get("_possibly_question_embedding"),
)
```

Data akhir yang digunakan oleh chat pipeline:

- `content`
- `embedding`
- `possibly_questions`
- `possibly_question_embedding`
- `section_title`
- `page_number`
- `chunk_metadata`

## Tahap Worker 13: Complete atau Failed

Jika semua berhasil:

```text
processing_status = completed
processing_progress = 100
processing_error = null
```

Jika terjadi error:

```python
db.rollback()
_update_processing_state(db, document_id, status="failed", error=error_msg)
```

Jika retry masih tersedia:

```python
self.retry(exc=e, countdown=30)
```

Artinya task akan dikirim ulang setelah 30 detik.

## Bagaimana RabbitMQ Membagi Task ke Banyak Worker

Misalnya ada 5 dokumen di-upload:

```text
doc1, doc2, doc3, doc4, doc5
```

FastAPI akan mengirim 5 task ke RabbitMQ.

Jika hanya ada 1 worker solo:

```text
worker1: doc1 -> doc2 -> doc3 -> doc4 -> doc5
```

Jika ada 2 worker solo:

```text
worker1: doc1 -> doc3 -> doc5
worker2: doc2 -> doc4
```

Pembagian sebenarnya tergantung worker mana yang selesai lebih dulu.

Karena `worker_prefetch_multiplier=1`, worker tidak akan mengambil terlalu banyak task sekaligus. Ini membuat distribusi task lebih adil.

## Kenapa Worker Pertama Tidak Terganggu Saat Worker Baru Ditambah?

RabbitMQ bersifat shared queue.

Worker yang sudah berjalan tetap memproses task yang sudah ia ambil.

Ketika worker baru dinyalakan:

1. worker baru connect ke RabbitMQ
2. worker baru subscribe ke queue yang sama
3. RabbitMQ mulai memberikan task berikutnya ke worker baru
4. worker lama tetap melanjutkan task yang sedang berjalan

Jadi menambah worker tidak menghentikan worker pertama.

Syaratnya:

- hostname worker berbeda
- worker memakai broker RabbitMQ yang sama
- worker berada di project/environment yang sama
- task module yang sama tersedia

Contoh:

```powershell
celery -A app.celery_app worker --loglevel=info --pool=solo --hostname=worker2@%h
```

## Hal yang Membuat Ingestion Lama

Faktor yang paling mempengaruhi:

1. jumlah halaman PDF
2. kualitas layout PDF
3. banyaknya tabel dan gambar
4. jumlah chunk yang dihasilkan
5. jumlah call question generator
6. jumlah call embedding
7. kecepatan GROBID
8. kecepatan Ollama/LLM melalui tunneling
9. CPU/RAM/GPU worker dan server Ollama
10. performa database saat insert vector

Tahap yang biasanya paling berat:

```text
GROBID/PyMuPDF extraction
-> question generation per chunk
-> question embedding per chunk
-> content embedding per chunk
-> insert vector ke database
```

## Risiko Jika Worker Terlalu Banyak

Menambah worker memang bisa memproses banyak dokumen bersamaan, tetapi tidak selalu membuat sistem lebih cepat.

Jika worker terlalu banyak:

- CPU penuh
- RAM naik
- Ollama antre terlalu panjang
- tunnel ke VPS menjadi bottleneck
- GROBID melambat
- database insert melambat
- task bisa timeout
- dokumen bisa gagal karena `task_time_limit`

Untuk VPS Ollama dengan 2 CPU core dan RTX A2000 12GB, nilai realistis biasanya:

```text
1 worker: paling aman
2 worker: ideal untuk penggunaan normal
3 worker: hanya untuk testing jika resource stabil
4+ worker: tidak disarankan
```

## Cara Mengecek Task dan Worker

Melihat worker aktif:

```bash
celery -A app.celery_app status
```

Melihat registered task:

```bash
celery -A app.celery_app inspect registered
```

Melihat task aktif:

```bash
celery -A app.celery_app inspect active
```

Melihat task yang sudah di-reserve worker:

```bash
celery -A app.celery_app inspect reserved
```

Melihat task yang dijadwalkan:

```bash
celery -A app.celery_app inspect scheduled
```

Jika memakai RabbitMQ management plugin, queue juga bisa dilihat dari dashboard RabbitMQ.

## Cara Menjalankan Worker

Worker solo:

```powershell
celery -A app.celery_app worker --loglevel=info --pool=solo
```

Worker solo dengan nama:

```powershell
celery -A app.celery_app worker --loglevel=info --pool=solo --hostname=worker1@%h
```

Worker kedua di terminal baru:

```powershell
celery -A app.celery_app worker --loglevel=info --pool=solo --hostname=worker2@%h
```

Jika tidak memakai `solo`, bisa memakai concurrency:

```powershell
celery -A app.celery_app worker --loglevel=info --concurrency=2
```

Namun di Windows, `--pool=solo` sering lebih stabil untuk development lokal.

## Ringkasan Akhir

Pipeline ingestion Syntra adalah proses asynchronous.

FastAPI bertugas menerima upload dan mengirim task.

RabbitMQ bertugas menyimpan dan membagikan task.

Celery worker bertugas memproses dokumen.

MinIO menyimpan PDF asli.

GROBID dan PyMuPDF mengekstrak isi PDF.

LLM dan embedding model memperkaya chunk agar retrieval lebih baik.

Database menyimpan hasil akhir dalam bentuk metadata dokumen, chunk, questions, dan vector embedding.

Alur paling ringkas:

```text
Upload PDF
-> FastAPI validasi dan simpan PDF
-> FastAPI publish task ke RabbitMQ
-> Celery worker consume task
-> Worker ekstrak metadata dan content
-> Worker chunking
-> Worker generate questions dan embeddings
-> Worker simpan DocumentChunk
-> Document completed
```

