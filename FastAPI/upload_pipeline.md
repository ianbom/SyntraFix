Fase 1 — Upload & Registrasi Dokumen
Teknologi: FastAPI, PostgreSQL, Celery
User mengupload file PDF melalui endpoint FastAPI. Sistem menyimpan file ke disk di direktori
Setelah insert berhasil dan document_id diperoleh, sistem mengirim task ke Celery sebagai message broker. Endpoint langsung return document_id dan status processing ke user tanpa menunggu proses selesai. Seluruh proses selanjutnya berjalan di background.

Fase 2 — GROBID: Ekstrak Metadata & Struktur Akademik
Teknologi: GROBID


Fase 3 — PyMuPDF: Ekstrak Teks, Gambar, dan Tabel
Teknologi: PyMuPDF (fitz), Python

Fase 4 — Normalisasi Data Visual
Teknologi: Python

Fase 5 — Smart Chunking
Semua elemen yang terkumpul dari fase 2, 3, dan 4 sekarang masuk ke proses chunking. Ada empat jalur paralel.
Jalur A — Chunking teks
Teknologi: langchain-text-splitters, tiktoken, nltk
Blok teks dari PyMuPDF diproses dengan menentukan chunk_type terlebih dahulu berdasarkan posisi dalam outline GROBID. Teks di bagian abstrak mendapat tipe ABSTRACT, teks di bagian referensi mendapat REFERENCE, judul dokumen mendapat TITLE, dan semua paragraf isi mendapat PARAGRAPH.
Teks yang panjang dipecah menggunakan RecursiveCharacterTextSplitter dengan ukuran 400 token dihitung menggunakan tiktoken. Overlap antar chunk menggunakan 2 kalimat terakhir dari chunk sebelumnya — sentence tokenization dilakukan dengan nltk untuk memastikan kalimat tidak terpotong di tengah.
Untuk setiap chunk dibuat dua versi: parent chunk sekitar 800 token yang akan dikirim ke LLM saat menjawab, dan child chunk sekitar 150 token yang dipakai untuk similarity search. parent_chunk_id disimpan di chunk_metadata milik child chunk.
Setelah ukuran chunk ditentukan, konteks struktural disimpan di `chunk_metadata` (bukan disisipkan ke konten). Field yang disimpan meliputi dokumen, section, sub-section (jika ada), dan nomor halaman.
Jalur B — Deskripsi tabel
Teknologi: PyMuPDF, Python
Hanya tabel yang memiliki caption valid seperti `Table 2.1 ...` atau `Tabel 3 ...` yang diproses.
Data tabel dari PyMuPDF dikirim ke LLM untuk diinterpretasikan menjadi teks naratif, dan nama tabel wajib muncul di awal konten (contoh: `Table 2.1 ...`).
Metadata konteks tabel (dokumen, section, halaman, caption, index tabel, ukuran tabel) disimpan di `chunk_metadata`. Tabel mentah (HTML/gambar) tidak disimpan ke database.
Jalur C — Deskripsi gambar
Teknologi: PyMuPDF, Python
Hanya gambar yang memiliki caption valid seperti `Gambar 2 ...` atau `Figure 4.1 ...` yang diproses.
Data gambar yang diekstrak dari PyMuPDF terlebih dahulu diinterpretasikan oleh LLM menjadi teks deskriptif, dan nama gambar wajib muncul di awal konten.
Metadata konteks gambar (dokumen, section, halaman, caption, format, dimensi, ukuran) disimpan di `chunk_metadata`. File gambar mentah tidak diupload ke MinIO dan tidak disimpan ke database.
Jalur D — Format referensi
Teknologi: Python pure logic
Data referensi terstruktur dari GROBID diformat menjadi teks naratif secara deterministik — tanpa perlu mengirim ke LLM karena data sudah terstruktur per field. Setiap entry referensi menjadi satu chunk dengan chunk_type = REFERENCE. Konteks section disimpan di `chunk_metadata` dengan section "Daftar Pustaka".
Progress diupdate ke processing_progress = 65.

Fase 6 — Generate Possibly Questions
Teknologi: LLM

Fase 7 — Generate Embedding

Fase 8 — Simpan ke Database
Teknologi: asyncpg, PostgreSQL, pgvector

