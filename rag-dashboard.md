# RENCANA IMPLEMENTASI DASHBOARD EVALUASI RAG SYNTRAAI

## 1. Tujuan Pengembangan

Dashboard Evaluasi RAG dikembangkan untuk menyediakan mekanisme pengujian kualitas sistem Retrieval-Augmented Generation secara terstruktur dan berulang. Sistem harus dapat:

1. menerima dataset pengujian dalam bentuk CSV yang diunggah oleh admin;
2. mengekspor percakapan chatbot menjadi CSV;
3. menjalankan evaluasi menggunakan RAGAS secara asynchronous;
4. menghitung Faithfulness, Answer Relevancy, Context Precision, dan Context Recall;
5. menampilkan progres pengujian secara otomatis;
6. menyimpan setiap pengujian sebagai batch yang berbeda;
7. menampilkan hasil evaluasi terbaru;
8. menyediakan riwayat dan detail evaluasi lama;
9. menyediakan hasil evaluasi per sampel;
10. mengekspor hasil evaluasi kembali menjadi CSV.

Istilah yang digunakan pada antarmuka sebaiknya adalah **Skor Evaluasi RAG**, bukan akurasi, karena keempat nilai tersebut bukan accuracy classification.

---

# 2. Gambaran Arsitektur

Arsitektur fitur evaluasi terdiri atas lima komponen utama:

1. **Dataset Management**

   * upload CSV;
   * validasi format;
   * preview data;
   * penyimpanan dataset;
   * ekspor chat menjadi CSV.

2. **Evaluation Run Management**

   * pembuatan batch pengujian;
   * penyimpanan konfigurasi;
   * pengelolaan status dan progress.

3. **RAG Pipeline Runner**

   * menjalankan pertanyaan melalui pipeline SyntraAI;
   * memperoleh response dan retrieved contexts.

4. **RAGAS Evaluation Worker**

   * menjalankan evaluasi di background menggunakan Celery;
   * menyimpan skor setiap sampel;
   * menghitung nilai agregat batch.

5. **Evaluation Dashboard**

   * menampilkan evaluasi terbaru;
   * menampilkan progress;
   * menampilkan grafik perkembangan;
   * menampilkan riwayat;
   * menampilkan detail setiap batch.

Alur keseluruhan:

```text
Admin
  │
  ├── Upload CSV
  │       │
  │       ▼
  │   Validasi dan Preview Dataset
  │       │
  │       ▼
  │   Simpan Dataset
  │
  ├── Export Chat CSV
  │       │
  │       ▼
  │   Edit atau Lengkapi Reference
  │       │
  │       ▼
  │   Upload sebagai Dataset Evaluasi
  │
  ▼
Buat Evaluation Run
  │
  ▼
Celery menjalankan pipeline RAG
  │
  ├── user_input
  ├── retrieved_contexts
  └── response
  │
  ▼
RAGAS Evaluation
  │
  ├── Faithfulness
  ├── Answer Relevancy
  ├── Context Precision
  └── Context Recall
  │
  ▼
Simpan hasil per sampel dan agregat
  │
  ▼
Dashboard diperbarui otomatis
```

---

# 3. Jenis Dataset Evaluasi

Sistem sebaiknya mendukung dua mode dataset.

## 3.1 Mode Pipeline Evaluation

Pada mode ini, CSV hanya menyediakan pertanyaan dan jawaban referensi. SyntraAI akan menjalankan pertanyaan melalui pipeline RAG untuk memperoleh response dan retrieved contexts.

Kolom wajib:

```csv
user_input,reference
"Apa fungsi metadata Dublin Core?","Dublin Core digunakan untuk mendeskripsikan dokumen menggunakan elemen metadata terstruktur."
```

Kolom tambahan yang disarankan:

```csv
test_case_id,user_input,reference,category,source_document_ids,notes
TC-001,"Apa fungsi metadata Dublin Core?","Dublin Core digunakan ...","metadata","[12,14]","Pertanyaan definisi"
```

Kolom:

| Kolom                 | Status   | Keterangan                              |
| --------------------- | -------- | --------------------------------------- |
| `test_case_id`        | Opsional | ID unik data uji                        |
| `user_input`          | Wajib    | Pertanyaan yang akan diuji              |
| `reference`           | Wajib    | Jawaban acuan                           |
| `category`            | Opsional | Kategori pertanyaan                     |
| `source_document_ids` | Opsional | Dokumen sumber yang mendukung reference |
| `notes`               | Opsional | Catatan validator                       |

Mode ini digunakan untuk menguji pipeline SyntraAI secara menyeluruh, mulai dari retrieval sampai generation.

## 3.2 Mode Score-Only Evaluation

Pada mode ini, CSV sudah berisi hasil percakapan dan konteks yang digunakan. Sistem hanya menjalankan RAGAS tanpa mengulangi pipeline RAG.

Kolom wajib:

```csv
user_input,response,retrieved_contexts,reference
```

Contoh:

```csv
user_input,response,retrieved_contexts,reference
"Apa itu RAG?","RAG menggabungkan retrieval dan generation.","[""RAG combines retrieval...""]","RAG adalah pendekatan yang menggabungkan retrieval dan generation."
```

Mode ini cocok untuk:

* mengevaluasi ulang percakapan yang sudah terjadi;
* mengevaluasi hasil model berbeda;
* menghindari generation ulang;
* membandingkan evaluator atau konfigurasi RAGAS.

---

# 4. Ketentuan Reference

Field `reference` merupakan jawaban acuan atau ground truth.

Reference diperlukan agar sistem dapat menghitung empat metrik secara lengkap, terutama Context Recall. Oleh karena itu:

* reference tidak diisi oleh pengguna chatbot biasa;
* reference disediakan oleh admin, peneliti, atau validator;
* reference dapat dibuat menggunakan bantuan LLM;
* reference yang dibuat LLM harus diperiksa manusia;
* hanya data dengan reference valid yang dapat digunakan pada evaluasi empat metrik.

Untuk CSV hasil ekspor chat, kolom reference dapat dibiarkan kosong:

```csv
conversation_id,chat_id,user_input,response,retrieved_contexts,reference
21,174,"Apa itu RAG?","RAG adalah ...","[""context...""]",""
```

Admin kemudian melengkapi kolom reference sebelum mengunggah CSV sebagai dataset evaluasi resmi.

Alternatifnya, sistem menyediakan menu editor reference pada halaman dataset.

---

# 5. Rancangan Database

## 5.1 Tabel `rag_evaluation_datasets`

Menyimpan informasi dataset hasil upload atau ekspor chat.

| Kolom               | Tipe        | Keterangan                           |
| ------------------- | ----------- | ------------------------------------ |
| `id`                | Integer     | Primary key                          |
| `name`              | Varchar     | Nama dataset                         |
| `description`       | Text        | Deskripsi dataset                    |
| `source_type`       | Varchar     | `csv_upload` atau `chat_export`      |
| `evaluation_mode`   | Varchar     | `pipeline` atau `score_only`         |
| `original_filename` | Varchar     | Nama file CSV                        |
| `file_path`         | Varchar     | Lokasi file di MinIO                 |
| `dataset_hash`      | Varchar     | Hash isi dataset                     |
| `total_rows`        | Integer     | Jumlah baris                         |
| `valid_rows`        | Integer     | Jumlah baris valid                   |
| `invalid_rows`      | Integer     | Jumlah baris tidak valid             |
| `status`            | Varchar     | uploaded, validating, ready, invalid |
| `validation_errors` | JSONB       | Daftar kesalahan validasi            |
| `created_by`        | Foreign Key | Admin pengunggah                     |
| `created_at`        | Timestamp   | Waktu upload                         |

## 5.2 Tabel `rag_evaluation_dataset_rows`

Menyimpan setiap baris dataset yang telah di-upload.

| Kolom                 | Keterangan                       |
| --------------------- | -------------------------------- |
| `id`                  | Primary key                      |
| `dataset_id`          | Relasi dataset                   |
| `row_number`          | Nomor baris CSV                  |
| `test_case_id`        | ID eksternal data uji            |
| `user_input`          | Pertanyaan                       |
| `reference`           | Jawaban acuan                    |
| `response`            | Jawaban hasil chat jika tersedia |
| `retrieved_contexts`  | Konteks dalam JSONB              |
| `category`            | Kategori data                    |
| `source_document_ids` | ID dokumen pendukung             |
| `validation_status`   | valid atau invalid               |
| `validation_message`  | Pesan kesalahan                  |

## 5.3 Tabel `rag_evaluation_runs`

Satu record mewakili satu batch pengujian.

| Kolom                   | Keterangan                                                    |
| ----------------------- | ------------------------------------------------------------- |
| `id`                    | ID batch                                                      |
| `dataset_id`            | Dataset yang digunakan                                        |
| `name`                  | Contoh: Testing 2 - 150 Data                                  |
| `description`           | Catatan pengujian                                             |
| `status`                | queued, running, completed, partial_failed, failed, cancelled |
| `evaluation_mode`       | pipeline atau score_only                                      |
| `total_samples`         | Jumlah seluruh sampel                                         |
| `processed_samples`     | Jumlah sampel selesai                                         |
| `successful_samples`    | Jumlah sampel valid                                           |
| `failed_samples`        | Jumlah sampel gagal                                           |
| `progress`              | Nilai 0–100                                                   |
| `faithfulness_avg`      | Rata-rata Faithfulness                                        |
| `answer_relevancy_avg`  | Rata-rata Answer Relevancy                                    |
| `context_precision_avg` | Rata-rata Context Precision                                   |
| `context_recall_avg`    | Rata-rata Context Recall                                      |
| `generator_model`       | Model generator                                               |
| `embedding_model`       | Model embedding                                               |
| `evaluator_model`       | Model evaluator RAGAS                                         |
| `ragas_version`         | Versi RAGAS                                                   |
| `config_snapshot`       | Konfigurasi pipeline dalam JSONB                              |
| `celery_task_id`        | ID task Celery                                                |
| `created_by`            | Admin pembuat batch                                           |
| `started_at`            | Waktu mulai                                                   |
| `completed_at`          | Waktu selesai                                                 |
| `error_message`         | Kesalahan batch                                               |
| `created_at`            | Waktu dibuat                                                  |

## 5.4 Tabel `rag_evaluation_samples`

Menyimpan hasil evaluasi setiap pertanyaan.

| Kolom                         | Keterangan                             |
| ----------------------------- | -------------------------------------- |
| `id`                          | ID sampel                              |
| `run_id`                      | Relasi batch                           |
| `dataset_row_id`              | Relasi data dataset                    |
| `sample_index`                | Urutan sampel                          |
| `user_input`                  | Snapshot pertanyaan                    |
| `reference`                   | Snapshot jawaban referensi             |
| `response`                    | Jawaban SyntraAI                       |
| `retrieved_contexts`          | Konteks yang digunakan                 |
| `references_metadata`         | Dokumen, chunk, halaman, dan skor      |
| `faithfulness`                | Skor per sampel                        |
| `answer_relevancy`            | Skor per sampel                        |
| `context_precision`           | Skor per sampel                        |
| `context_recall`              | Skor per sampel                        |
| `rag_duration_seconds`        | Waktu pipeline RAG                     |
| `evaluation_duration_seconds` | Waktu RAGAS                            |
| `status`                      | pending, processing, completed, failed |
| `error_message`               | Kesalahan sampel                       |
| `completed_at`                | Waktu selesai                          |

## 5.5 Tabel `rag_evaluation_artifacts`

Menyimpan file hasil evaluasi.

| Kolom           | Keterangan                                    |
| --------------- | --------------------------------------------- |
| `id`            | Primary key                                   |
| `run_id`        | Relasi batch                                  |
| `artifact_type` | input_csv, result_csv, error_csv, config_json |
| `file_path`     | Lokasi di MinIO                               |
| `filename`      | Nama file                                     |
| `created_at`    | Waktu pembuatan                               |

---

# 6. Fitur Upload CSV

## 6.1 Alur Upload

1. Admin membuka halaman Dataset Evaluasi.
2. Admin memilih file CSV.
3. Admin memilih mode:

   * Pipeline Evaluation;
   * Score-Only Evaluation.
4. Backend menyimpan file asli ke MinIO.
5. Backend membaca header CSV.
6. Sistem memvalidasi setiap baris.
7. Sistem menampilkan preview.
8. Admin mengonfirmasi penyimpanan dataset.
9. Dataset berubah menjadi status `ready`.

## 6.2 Validasi CSV

Validasi file:

* hanya menerima `.csv`;
* encoding UTF-8;
* ukuran file dibatasi;
* header harus sesuai;
* tidak boleh mengandung file kosong;
* jumlah baris harus lebih dari nol.

Validasi Pipeline Evaluation:

* `user_input` wajib;
* `reference` wajib;
* pertanyaan tidak boleh kosong;
* reference tidak boleh kosong.

Validasi Score-Only Evaluation:

* `user_input` wajib;
* `response` wajib;
* `retrieved_contexts` wajib;
* `reference` wajib;
* `retrieved_contexts` harus berupa JSON array valid.

## 6.3 Hasil Validasi

Halaman preview menampilkan:

| Baris | User Input        | Reference     | Status  | Pesan                 |
| ----: | ----------------- | ------------- | ------- | --------------------- |
|     1 | Apa itu RAG?      | RAG adalah... | Valid   | -                     |
|     2 | Apa itu metadata? | Kosong        | Invalid | Reference wajib diisi |

Admin dapat:

* membatalkan upload;
* menghapus baris invalid;
* mengunduh laporan error;
* memperbaiki CSV dan upload ulang;
* menyimpan hanya baris valid.

Untuk batch evaluasi resmi, sebaiknya seluruh baris harus valid.

---

# 7. Fitur Export Chat ke CSV

## 7.1 Lokasi Fitur

Fitur export dapat ditempatkan pada:

* halaman riwayat conversation;
* halaman dashboard evaluasi;
* halaman khusus Chat Dataset Export.

## 7.2 Filter Export

Admin dapat memilih:

* rentang tanggal;
* pengguna;
* conversation tertentu;
* seluruh conversation;
* jumlah chat;
* status chat;
* hanya chat yang memiliki reference dokumen;
* hanya chat dengan response yang berhasil.

## 7.3 Isi CSV Export

Kolom yang disarankan:

```csv
conversation_id,
conversation_title,
chat_user_id,
user_message_id,
bot_message_id,
user_input,
response,
retrieved_contexts,
document_references,
reference,
created_at
```

Contoh:

```csv
conversation_id,conversation_title,user_input,response,retrieved_contexts,document_references,reference
12,"Diskusi RAG","Apa itu RAG?","RAG adalah ...","[""RAG combines retrieval...""]","[{""document_id"":3,""chunk_id"":22,""page"":4}]",""
```

Field `reference` secara default kosong karena percakapan pengguna tidak memiliki ground truth.

## 7.4 Dua Cara Menggunakan Hasil Export

### Cara pertama: Edit CSV

1. Admin mengekspor chat.
2. Admin membuka CSV.
3. Admin mengisi kolom reference.
4. Admin mengunggah CSV sebagai Score-Only Evaluation.
5. Sistem menjalankan RAGAS.

### Cara kedua: Validasi melalui Website

1. Hasil export disimpan sebagai dataset draft.
2. Admin membuka halaman Dataset Detail.
3. Admin mengisi reference pada setiap baris.
4. Baris diberi status `validated`.
5. Dataset dijalankan sebagai evaluasi.

Cara kedua lebih terintegrasi, tetapi membutuhkan halaman editor tambahan.

---

# 8. Proses Evaluation Run

## 8.1 Membuat Batch

Admin memilih:

* dataset;
* nama batch;
* deskripsi;
* mode evaluasi;
* model evaluator;
* konfigurasi evaluasi;
* apakah hanya menjalankan data valid.

Contoh:

```text
Nama batch:
Testing 2 - 150 Data

Dataset:
Dataset RAG V2

Mode:
Pipeline Evaluation

Generator:
llama3.1:8b-instruct-q8_0

Embedding:
bge-m3:567m

Evaluator:
llama3.1:8b-instruct-q8_0
```

## 8.2 Snapshot Konfigurasi

Setiap batch harus menyimpan konfigurasi:

```json
{
  "generator_model": "llama3.1:8b-instruct-q8_0",
  "embedding_model": "bge-m3:567m",
  "evaluator_model": "llama3.1:8b-instruct-q8_0",
  "top_k_candidates": 20,
  "final_context_count": 8,
  "similarity_threshold": 0.35,
  "metadata_filter": true,
  "query_expansion": true,
  "possibly_question_embedding": true,
  "reranker": true,
  "prompt_version": "rag-prompt-v3",
  "ragas_version": "versi-yang-digunakan"
}
```

Konfigurasi lama tidak boleh ikut berubah ketika konfigurasi aplikasi diperbarui.

## 8.3 Status Evaluation Run

Lifecycle batch:

```text
queued
  ↓
preparing
  ↓
running_rag
  ↓
running_ragas
  ↓
aggregating
  ↓
completed
```

Kemungkinan status lain:

```text
partial_failed
failed
cancelled
```

## 8.4 Background Processing

Evaluasi dijalankan melalui Celery dan RabbitMQ agar request HTTP tidak menunggu proses selesai.

Worker melakukan:

1. mengambil data dataset;
2. membuat evaluation samples;
3. menjalankan pipeline RAG jika mode pipeline;
4. menjalankan RAGAS per kelompok data;
5. menyimpan skor per sampel;
6. memperbarui progress;
7. menghitung agregat;
8. membuat file result CSV;
9. mengubah status menjadi completed.

Gunakan queue khusus:

```text
ragas_evaluation
```

Worker evaluation sebaiknya memiliki concurrency rendah, misalnya satu task pada satu waktu, karena Ollama dan RAGAS menggunakan sumber daya GPU yang besar.

---

# 9. Automatic Dashboard Update

Untuk versi awal, gunakan polling melalui React Query.

Interval:

```text
3–5 detik selama terdapat run aktif
```

Alur:

1. frontend memanggil endpoint latest dan active run;
2. selama status `queued` atau `running`, data diperbarui setiap tiga detik;
3. ketika status completed, polling dihentikan;
4. query latest, history, dan detail di-refresh;
5. dashboard otomatis menampilkan hasil terbaru.

WebSocket atau Server-Sent Events dapat ditambahkan kemudian, tetapi polling lebih sederhana dan sudah sesuai dengan pola monitoring dokumen pada SyntraAI.

Dashboard harus membedakan:

* **Active Evaluation**, yaitu batch yang sedang berjalan;
* **Latest Completed Evaluation**, yaitu batch terakhir yang selesai.

Dengan demikian, metrik utama tidak berubah menjadi kosong ketika batch baru sedang diproses.

---

# 10. Halaman Frontend

## 10.1 Dashboard Evaluasi RAG

Route:

```text
/admin/rag-evaluation
```

Isi halaman:

### A. Active Evaluation

Ditampilkan hanya jika terdapat proses aktif.

```text
Testing 3 - 200 Data
Status: Running RAGAS
Processed: 84 / 200
Progress: 42%
Successful: 82
Failed: 2
Elapsed Time: 38 menit
```

Tombol:

* Lihat progress;
* Batalkan;
* Lihat error sementara.

### B. Latest Completed Evaluation

Empat kartu utama:

```text
Faithfulness        82,2%
Answer Relevancy    84,0%
Context Precision   80,2%
Context Recall      83,6%
```

Setiap kartu menampilkan:

* skor;
* kategori skor;
* perubahan dari batch sebelumnya;
* jumlah sampel valid.

Contoh:

```text
Faithfulness
83,4%
Naik 1,2% dari batch sebelumnya
147 sampel valid
```

### C. Informasi Batch Terbaru

Menampilkan:

* nama batch;
* dataset;
* total data;
* data berhasil;
* data gagal;
* waktu mulai;
* waktu selesai;
* durasi;
* model generator;
* model embedding;
* evaluator;
* versi RAGAS.

### D. Grafik Tren Riwayat

Grafik garis dengan:

* sumbu X: nama atau tanggal batch;
* sumbu Y: skor 0–1;
* empat garis metrik.

Data contoh:

| Batch     | Data | Faithfulness | Answer Relevancy | Context Precision | Context Recall |
| --------- | ---: | -----------: | ---------------: | ----------------: | -------------: |
| Testing 1 |  100 |        0,822 |            0,840 |             0,802 |          0,836 |
| Testing 2 |  150 |        0,834 |            0,851 |             0,817 |          0,842 |

### E. Distribusi Skor Terbaru

Distribusi:

| Kelompok    | Faithfulness | Answer Relevancy | Context Precision | Context Recall |
| ----------- | -----------: | ---------------: | ----------------: | -------------: |
| `< 0,50`    |           10 |                9 |                18 |             10 |
| `0,50–0,80` |           42 |               18 |                26 |             32 |
| `> 0,80`    |           78 |              101 |                86 |             88 |

### F. Riwayat Evaluasi

Tabel:

| Batch     | Dataset | Sampel | Faithfulness | Answer Relevancy | Context Precision | Context Recall | Status    | Tanggal |
| --------- | ------- | -----: | -----------: | ---------------: | ----------------: | -------------: | --------- | ------- |
| Testing 2 | RAG V2  |    150 |        0,834 |            0,851 |             0,817 |          0,842 | Completed | 20 Juni |
| Testing 1 | RAG V1  |    100 |        0,822 |            0,840 |             0,802 |          0,836 | Completed | 10 Juni |

Fitur tabel:

* pagination;
* pencarian nama batch;
* filter status;
* filter dataset;
* filter tanggal;
* urutkan berdasarkan nilai;
* tombol Detail;
* tombol Export Result.

---

## 10.2 Halaman Dataset Evaluasi

Route:

```text
/admin/rag-evaluation/datasets
```

Isi:

* daftar dataset;
* tombol Upload CSV;
* tombol Download Template;
* tombol Export Chat;
* status validasi;
* total baris;
* jumlah baris valid dan invalid;
* tanggal dibuat;
* tombol Preview;
* tombol Start Evaluation;
* tombol Delete.

---

## 10.3 Halaman Upload Dataset

Route:

```text
/admin/rag-evaluation/datasets/upload
```

Tahapan halaman:

```text
1. Pilih file
2. Pilih mode
3. Validasi
4. Preview
5. Konfirmasi
```

Informasi yang ditampilkan:

* nama file;
* ukuran;
* header yang ditemukan;
* total baris;
* baris valid;
* baris invalid;
* daftar kesalahan.

---

## 10.4 Halaman Detail Dataset

Route:

```text
/admin/rag-evaluation/datasets/:datasetId
```

Isi:

* informasi dataset;
* file sumber;
* jumlah data;
* mode;
* preview seluruh baris;
* status reference;
* editor reference;
* filter data invalid;
* download CSV;
* start evaluation.

---

## 10.5 Halaman Detail Evaluasi Lama

Route:

```text
/admin/rag-evaluation/runs/:runId
```

Halaman ini harus tetap dapat dibuka walaupun terdapat evaluasi baru.

Isi halaman:

### Ringkasan

* nama batch;
* deskripsi;
* dataset;
* jumlah sampel;
* status;
* waktu mulai dan selesai;
* durasi;
* empat skor agregat.

### Konfigurasi

* generator model;
* embedding model;
* evaluator model;
* versi RAGAS;
* top-k;
* threshold;
* jumlah konteks;
* metadata filtering;
* query expansion;
* reranker;
* prompt version.

### Distribusi

* distribusi empat metrik;
* rata-rata;
* median;
* minimum;
* maksimum;
* standard deviation.

### Tabel Sampel

| No | Pertanyaan      | Faithfulness | Answer Relevancy | Context Precision | Context Recall | Status    |
| -: | --------------- | -----------: | ---------------: | ----------------: | -------------: | --------- |
|  1 | Apa itu RAG?    |         0,90 |             0,95 |              0,85 |           1,00 | Completed |
|  2 | Apa fungsi DOI? |         0,40 |             0,71 |              0,35 |           0,50 | Completed |

Filter sampel:

* skor rendah;
* skor tinggi;
* sampel gagal;
* kategori;
* pertanyaan;
* dokumen sumber.

### Detail Satu Sampel

Saat baris dipilih, tampilkan:

* user input;
* reference;
* response;
* retrieved contexts;
* dokumen sumber;
* chunk;
* nomor halaman;
* skor setiap metrik;
* waktu RAG;
* waktu evaluasi;
* error jika ada.

Tombol:

* Export Result CSV;
* Export Failed Samples;
* Rerun Failed Samples;
* Duplicate Run;
* Compare with Another Run.

---

# 11. Endpoint Backend

## 11.1 Dataset

```text
POST   /rag-evaluation/datasets/upload
GET    /rag-evaluation/datasets
GET    /rag-evaluation/datasets/{dataset_id}
GET    /rag-evaluation/datasets/{dataset_id}/rows
PATCH  /rag-evaluation/datasets/{dataset_id}/rows/{row_id}
DELETE /rag-evaluation/datasets/{dataset_id}
GET    /rag-evaluation/datasets/template
GET    /rag-evaluation/datasets/{dataset_id}/download
```

## 11.2 Export Chat

```text
POST /rag-evaluation/chat-export
GET  /rag-evaluation/chat-export/{export_id}/download
```

Request:

```json
{
  "date_from": "2026-06-01",
  "date_to": "2026-06-20",
  "user_ids": [],
  "conversation_ids": [],
  "only_with_references": true,
  "create_dataset": true
}
```

## 11.3 Evaluation Run

```text
POST   /rag-evaluation/runs
GET    /rag-evaluation/runs
GET    /rag-evaluation/runs/latest
GET    /rag-evaluation/runs/active
GET    /rag-evaluation/runs/{run_id}
GET    /rag-evaluation/runs/{run_id}/samples
POST   /rag-evaluation/runs/{run_id}/cancel
POST   /rag-evaluation/runs/{run_id}/retry-failed
POST   /rag-evaluation/runs/{run_id}/duplicate
GET    /rag-evaluation/runs/{run_id}/export
GET    /rag-evaluation/runs/{run_id}/errors/export
```

## 11.4 Dashboard

```text
GET /rag-evaluation/dashboard/summary
GET /rag-evaluation/dashboard/history
GET /rag-evaluation/dashboard/distribution
GET /rag-evaluation/dashboard/compare
```

---

# 12. Struktur Folder Implementasi

## Backend

```text
FastAPI/app/
├── api/routes/
│   └── rag_evaluations.py
├── models/
│   ├── rag_evaluation_dataset.py
│   ├── rag_evaluation_run.py
│   └── rag_evaluation_sample.py
├── schemas/
│   └── rag_evaluation.py
├── services/
│   ├── rag_evaluation/
│   │   ├── csv_importer.py
│   │   ├── csv_validator.py
│   │   ├── chat_exporter.py
│   │   ├── dataset_service.py
│   │   ├── evaluation_service.py
│   │   ├── aggregation_service.py
│   │   └── artifact_service.py
│   ├── rag_pipeline.py
│   └── ragas_evaluator.py
└── tasks/
    └── rag_evaluation_tasks.py
```

## Frontend

```text
syntra-frontend/src/pages/admin/rag-evaluation/
├── api.ts
├── types.ts
├── dashboard.tsx
├── datasets.tsx
├── dataset-upload.tsx
├── dataset-detail.tsx
├── run-detail.tsx
├── components/
│   ├── active-run-card.tsx
│   ├── metric-card.tsx
│   ├── metric-trend-chart.tsx
│   ├── score-distribution-chart.tsx
│   ├── run-history-table.tsx
│   ├── sample-result-table.tsx
│   ├── csv-preview-table.tsx
│   └── run-config-card.tsx
```

---

# 13. Tahapan Implementasi

## Tahap 1 — Database dan Model

Pekerjaan:

* membuat tabel dataset;
* membuat tabel dataset rows;
* membuat tabel runs;
* membuat tabel samples;
* membuat tabel artifacts;
* membuat migration Alembic;
* membuat relasi SQLAlchemy.

Hasil:

* struktur data batch dan riwayat tersedia;
* pengujian lama tidak akan tertimpa.

## Tahap 2 — CSV Import dan Validation

Pekerjaan:

* endpoint upload;
* simpan file ke MinIO;
* parser CSV;
* validasi header;
* validasi per baris;
* preview data;
* laporan kesalahan;
* template CSV.

Hasil:

* admin dapat mengunggah dataset 100 atau 150 data;
* kesalahan CSV dapat diketahui sebelum evaluasi.

## Tahap 3 — Chat Export

Pekerjaan:

* query conversation, chats, chat references, dan document chunks;
* pasangkan pesan user dan bot;
* kumpulkan contexts;
* kumpulkan metadata dokumen;
* hasilkan CSV;
* opsi langsung membuat dataset draft.

Hasil:

* data percakapan dapat digunakan kembali sebagai data evaluasi.

## Tahap 4 — Refactor Pipeline RAG

Pekerjaan:

* memisahkan logika RAG dari penyimpanan chat;
* membuat method yang menerima pertanyaan;
* mengembalikan response, contexts, dan references;
* menyediakan mode `persist_chat=False`.

Hasil:

* evaluasi otomatis tidak memenuhi tabel chat pengguna.

## Tahap 5 — RAGAS Worker

Pekerjaan:

* mengintegrasikan RAGAS ke backend;
* membuat task Celery;
* evaluasi dalam batch kecil;
* penyimpanan skor per sampel;
* progress tracking;
* penanganan NaN;
* retry sampel gagal;
* agregasi skor.

Hasil:

* evaluasi dapat berjalan tanpa memblokir API.

## Tahap 6 — Evaluation API

Pekerjaan:

* create run;
* latest run;
* active run;
* history;
* detail;
* samples;
* cancel;
* retry;
* duplicate;
* result export.

Hasil:

* seluruh data dashboard tersedia melalui API.

## Tahap 7 — Frontend Dashboard

Pekerjaan:

* empat metric cards;
* progress aktif;
* grafik tren;
* distribusi skor;
* riwayat batch;
* halaman detail;
* sample viewer;
* polling otomatis.

Hasil:

* admin dapat melihat evaluasi terbaru dan lama.

## Tahap 8 — Pengujian

Urutan pengujian:

```text
5 data
20 data
100 data
150 data
```

Pengujian mencakup:

* CSV valid;
* CSV invalid;
* reference kosong;
* retrieved contexts tidak valid;
* task dihentikan;
* server restart;
* sampel RAGAS gagal;
* batch selesai;
* riwayat tidak tertimpa;
* export result dapat dibuka.

---

# 14. Acceptance Criteria

Fitur dinyatakan selesai apabila:

1. admin dapat mengunggah CSV melalui website;
2. sistem dapat mendeteksi baris CSV yang tidak valid;
3. admin dapat melihat preview sebelum menjalankan evaluasi;
4. admin dapat mengekspor chat menjadi CSV;
5. CSV hasil export dapat digunakan kembali sebagai dataset;
6. sistem dapat menjalankan batch dengan jumlah data berbeda;
7. setiap batch disimpan sebagai record terpisah;
8. progress batch diperbarui otomatis;
9. dashboard menampilkan evaluasi terakhir yang selesai;
10. dashboard menampilkan batch yang sedang berjalan;
11. empat skor RAGAS ditampilkan;
12. jumlah data valid dan gagal ditampilkan;
13. grafik tren antarbatch tersedia;
14. detail evaluasi lama tetap dapat dibuka;
15. skor per sampel dapat diperiksa;
16. konfigurasi setiap batch tersimpan;
17. hasil evaluasi dapat diekspor;
18. batch lama tidak berubah ketika dataset sumber diedit;
19. hanya admin yang dapat mengakses fitur;
20. sampel tanpa reference tidak dihitung pada evaluasi empat metrik.

---

# 15. Prioritas MVP

Fitur MVP yang sebaiknya dikerjakan terlebih dahulu:

1. upload CSV Pipeline Evaluation;
2. validasi `user_input` dan `reference`;
3. tabel evaluation runs dan samples;
4. Celery task RAG dan RAGAS;
5. progress polling;
6. empat metric cards;
7. tabel history;
8. halaman detail batch;
9. export result CSV;
10. export chat CSV.

Fitur lanjutan:

* editor reference di website;
* compare dua batch;
* duplicate run;
* rerun failed samples;
* distribusi kategori;
* WebSocket progress;
* automatic reference candidate;
* notifikasi ketika evaluasi selesai.

---

# 16. Keputusan Desain Utama

Beberapa keputusan yang perlu dipertahankan dalam implementasi:

* satu pengujian selalu menghasilkan satu evaluation run baru;
* hasil pengujian lama tidak boleh ditimpa;
* dataset dan konfigurasi disimpan sebagai snapshot;
* PostgreSQL menjadi sumber data utama dashboard;
* MinIO menyimpan file CSV dan artifacts;
* Celery digunakan untuk pemrosesan background;
* polling digunakan untuk pembaruan awal dashboard;
* skor per sampel selalu disimpan;
* rata-rata dihitung hanya dari sampel valid;
* jumlah sampel gagal selalu ditampilkan;
* reference wajib untuk evaluasi empat metrik;
* latest evaluation berarti evaluation run terakhir yang berstatus completed;
* active evaluation ditampilkan secara terpisah dari latest completed evaluation.
