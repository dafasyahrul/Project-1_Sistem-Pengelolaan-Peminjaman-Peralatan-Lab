# Sistem Peminjaman Peralatan Laboratorium

Proyek kelompok Praktikum Pemrograman Dasar. Aplikasi CLI berbasis Python (OOP)
untuk mengelola mahasiswa, alat, dan transaksi peminjaman.

## Struktur
```
main.py                      # titik masuk program
menu_app.py                  # antarmuka menu
models/                      # enums, mahasiswa, alat, transaksi
managers/                    # mahasiswa_manager, alat_manager, transaksi_manager
```

## Menjalankan
```
python main.py            # data kosong
python main.py --demo     # dengan data contoh
```
Membutuhkan Python 3.10+.

## Aturan bisnis
- Maksimal 2 transaksi aktif per mahasiswa
- Lama peminjaman maksimal 7 hari
- Mahasiswa yang punya transaksi aktif tidak bisa dihapus
- Alat yang sedang dipinjam tidak bisa dihapus

## Kesepakatan antar modul
- Semua kegagalan dilempar sebagai `ValueError("pesan")`, ditangkap oleh `MenuApp`.
- `buat_transaksi(nim, items, lama_hari)`: `items` = list tuple `(kode_alat, jumlah)`.
- `cari_by_mahasiswa` = semua transaksi mahasiswa; `riwayat_mahasiswa` = hanya yang SELESAI.
- `Transaksi.catat_pengembalian` mengubah item, stok `Alat`, dan status sekaligus.
- `TransaksiManager` yang menambah/menghapus ID transaksi aktif di `Mahasiswa`.

## Anggota
| Nama | Bagian |
|---|---|
| (isi) | Enums, Mahasiswa, MahasiswaManager, MenuApp |
| (isi) | Alat, AlatManager |
| (isi) | Transaksi, ItemPeminjaman, Pengembalian |
| (isi) | TransaksiManager, main.py, integrasi |