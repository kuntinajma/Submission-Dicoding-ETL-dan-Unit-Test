# ETL Pipeline Project

## Deskripsi Proyek

Proyek ini adalah pembuatan ETL (Extract, Transform, Load) pipeline untuk mengambil data produk dari website **Fashion Studio Dicoding**, melakukan transformasi pada data, dan memuatnya ke dalam beberapa repositori data seperti file CSV, Google Sheets, dan PostgreeSQL. Proyek ini juga dilengkapi dengan unit testing untuk memvalidasi setiap tahapan dalam ETL pipeline.

### Fitur Utama:
- **Extract:** Mengambil data produk dari website https://fashion-studio.dicoding.dev/.
- **Transform:** Membersihkan dan memodifikasi data, termasuk mengonversi harga menjadi rupiah, menghapus data invalid, dan memastikan tipe data yang sesuai.
- **Load:** Menyimpan data yang sudah dibersihkan ke dalam file CSV, Google Sheets, dan PostgreeSQL.
- **Unit Testing:** Melakukan pengujian unit pada setiap tahapan ETL.

## Penjelasan Berkas

- **`tests/test_extract.py`**: Mengandung unit test untuk tahapan ekstraksi data (scraping).
- **`tests/test_transform.py`**: Mengandung unit test untuk tahapan transformasi data.
- **`tests/test_load.py`**: Mengandung unit test untuk tahapan loading data.
- **`utils/extract.py`**: Berisi fungsi untuk mengekstrak data dari website.
- **`utils/transform.py`**: Berisi fungsi untuk mentransformasikan data, termasuk konversi harga dan pembersihan data.
- **`utils/load.py`**: Berisi fungsi untuk memuat data ke dalam file CSV, Google Sheets, dan PostgreeSQL.
- **`main.py`**: Menjalankan keseluruhan pipeline ETL.
- **`requirements.txt`**: Daftar dependensi Python untuk proyek ini.
- **`google-sheets-api.json`**: File service account untuk akses Google Sheets API (Tidak saya upload karena alasan keamanan0
- **`products.csv`**: File CSV tempat data yang sudah dibersihkan disimpan.

## Dependensi

Sebelum menjalankan proyek, pastikan untuk menginstal dependensi yang diperlukan. Anda dapat menginstalnya dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
````

## Cara Menjalankan

1. Pastikan Anda sudah mengaktifkan virtual environment.
2. Jalankan `main.py` untuk mengeksekusi pipeline ETL:

```bash
python main.py
```

3. Data yang telah diproses akan disimpan dalam file `products.csv` dan juga akan dimuat ke dalam Google Sheets.

## Unit Testing

Unit testing dilakukan untuk memastikan setiap fungsi dalam pipeline ETL berjalan sesuai dengan yang diharapkan. 

### Hasil Test Coverage

Berikut adalah hasil test coverage dari proyek ini:

```
Name                      Stmts   Miss  Cover
---------------------------------------------
tests\test_extract.py        28      2    93%
tests\test_load.py           21      1    95%
tests\test_transform.py      19      1    95%
utils\extract.py             30      3    90%
utils\load.py                27     11    59%
utils\transform.py           28      0   100%
---------------------------------------------
TOTAL                       153     18    88%
```

Dengan total coverage **88%**, proyek ini memenuhi kriteria untuk **Advanced** dalam penilaian unit testing.

## Kriteria Penilaian

### Kriteria 1: Membuat ETL Pipeline dengan Prinsip Modular Code

* Kode dibagi menjadi tiga modul terpisah: **Extract**, **Transform**, dan **Load**.
* Mengambil data dari website [https://fashion-studio.dicoding.dev/](https://fashion-studio.dicoding.dev/).
* Data yang diproses mencakup Title, Price, Rating, Colors, Size, dan Gender.
* Data yang diproses telah dibersihkan dan dikonversi sesuai ketentuan, termasuk konversi harga ke dalam mata uang Rupiah (Rp16.000).
* Data yang dihasilkan tidak mengandung nilai null, duplikat, atau invalid.

### Kriteria 2: Menyimpan Data dalam Repositori Data

* Data disimpan dalam format CSV dan juga dimuat ke dalam Google Sheets, dan PostgreeSQL.
* Menggunakan Google Sheets API dengan service account yang disediakan.

### Kriteria 3: Menerapkan Unit Test

* Unit testing diterapkan pada setiap tahapan ETL (extract, transform, load).
* Test coverage mencapai **88%**, memenuhi kriteria untuk **Advanced**.
