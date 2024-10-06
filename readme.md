| Name          | NRP        | Kelas                 |
| ------------- | ---------- | --------------------- |
| Lucky Santoso | 5025221050 | Keamaan Informasi (B) |

# Implementasi DES (Data Encryption Standard)

implementasi dari algoritma DES, yaitu salah satu algoritma kriptografi simetris yang digunakan untuk mengenkripsi dan mendekripsi data. DES menggunakan kunci 64-bit dan memproses data dalam blok 64-bit. Algoritma ini terdiri dari beberapa langkah, termasuk permutasi, rotasi, dan penggunaan fungsi Feistel.

## Struktur Program

- Fungsi Pemrosesan Bit: Mengonversi teks ke dalam representasi bit dan sebaliknya.
- Tabel Permutasi: Tabel untuk permutasi input, ekspansi, dan pemilihan kunci.
- Fungsi Kunci: Menghasilkan kunci sub dari kunci utama.
- Fungsi Feistel: Melakukan operasi pada setengah blok data menggunakan kunci sub.
- Enkripsi dan Dekripsi: Menggunakan fungsi Feistel dan kunci sub untuk mengenkripsi dan mendekripsi data.

Input

- Kunci: Masukkan kunci untuk proses enkripsi. Kunci harus berupa string dengan panjang 8 karakter (64 bit).
- Teks: Masukkan teks yang ingin dienkripsi. Teks dapat berupa string dengan panjang variabel.

Output

- Masukkan teks terenkripsi dan algoritma akan menghasilkan teks asli.

# Implementasi DES dengan ECB (Electronic Code Book)

ECB (Electronic Codebook) adalah salah satu mode operasi dalam algoritma kriptografi yang digunakan untuk mengenkripsi data. Plaintext dibagi menjadi blok-blok yang sama besar dan setiap blok dienkripsi secara terpisah menggunakan kunci yang sama.

**Alur Program**

- Input: Data plaintext yang akan dienkripsi.

- Data plaintext dibagi menjadi blok-blok.
  Setiap blok dienkripsi secara independen menggunakan algoritma enkripsi DES. Hasil enkripsi untuk setiap blok digabungkan menjadi ciphertext.

- Output: Ciphertext yang dihasilkan dari enkripsi blok-blok plaintext.

**Kelebihan Algoritma ECB**

- Mudah diimplementasikan karena setiap blok diproses secara terpisah.

- Paralelisme: Dapat mengenkripsi blok-blok secara paralel, sehingga dapat meningkatkan kecepatan enkripsi.

**Kekurangan Algoritma ECB**

- Keamanan Rendah jika dua blok plaintext identik, hasil ciphertext-nya juga identik. Hal ini bisa mengungkap pola dalam data dan memungkinkan penyerang untuk melakukan analisis lebih lanjut.

- Pola yang sama dalam plaintext menghasilkan pola yang sama dalam ciphertext, ini dapat digunakan untuk memecahkan enkripsi.

# Implementasi DES dengan CBC (Cipher Block Chaining)

Cipher Block Chaining (CBC) adalah mode operasi untuk kriptografi blok yang menggabungkan setiap blok plaintext dengan blok ciphertext sebelumnya sebelum dienkripsi. Setiap blok plaintext di-XOR dengan ciphertext blok sebelumnya.

**Alur Program**

- Bagi plaintext menjadi blok-blok berukuran tetap
- Tambahkan padding jika panjang plaintext tidak kelipatan dari ukuran blok.
  Inisialisasi Vektor (IV):
- Buat vektor inisialisasi (IV) yang acak dan unik untuk setiap proses enkripsi.

Proses Enkripsi:

Untuk blok pertama (C1):

- Gabungkan plaintext pertama (P1) dengan IV menggunakan operasi XOR.
- Enkripsi hasil XOR menggunakan algoritma simetris (misalnya, AES) untuk menghasilkan ciphertext pertama (C1).

Untuk setiap blok berikutnya (Ci) :

- Gabungkan plaintext (Pi) dengan ciphertext blok sebelumnya (Ci-1) menggunakan operasi XOR.
- Enkripsi hasil XOR untuk menghasilkan ciphertext (Ci).
  Hasil:

- Gabungkan semua ciphertext (C1, C2, ..., Cn) untuk membentuk ciphertext lengkap.
  Kirimkan IV dan ciphertext ke penerima.

Dekripsi:

Penerima menggunakan IV dan ciphertext serta key untuk mendekripsi.

**Kelebihan**

- Keamanan Lebih Tinggi dengan mengurangi pola dalam ciphertext dibandingkan dengan mode ECB.
- Menghasilkan ciphertext yang berbeda untuk blok plaintext yang identik.

**Kekurangan**

- Proses enkripsi lebih lambat karena ketergantungan antar blok.
- Harus menggunakan IV yang unik dan acak, yang harus dikelola dengan baik.
- Kerusakan pada satu blok dapat mempengaruhi semua blok berikutnya.
