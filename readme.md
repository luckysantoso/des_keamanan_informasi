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
