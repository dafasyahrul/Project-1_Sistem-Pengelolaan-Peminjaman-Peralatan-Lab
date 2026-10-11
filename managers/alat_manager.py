"""Pengelola data Alat dan kategori."""
from models.alat import Alat


class AlatManager:
    KATEGORI_AWAL = ("Elektronik", "Mekanik", "Optik", "Umum")

    def __init__(self):
        self.__data: dict[str, Alat] = {}  
        self.__daftar_kategori: set[str] = set(self.KATEGORI_AWAL)

   
    def tambah_kategori(self, nama: str) -> None:
        nama = nama.strip().title()
        if not nama:
            raise ValueError("Nama kategori tidak boleh kosong.")
        if nama in self.__daftar_kategori:
            raise ValueError(f"Kategori '{nama}' sudah ada.")
        self.__daftar_kategori.add(nama)

    def semua_kategori(self) -> list[str]:
        return sorted(self.__daftar_kategori)

    def __normalisasi_kategori(self, kategori: str) -> str:
        kategori = kategori.strip().title()
        if kategori not in self.__daftar_kategori:
            raise ValueError(
                f"Kategori '{kategori}' belum ada. Pilihan: "
                f"{', '.join(self.semua_kategori())} (atau tambah kategori dulu)."
            )
        return kategori

  
    def tambah(self, kode: str, nama: str, kategori: str, stok: int) -> Alat:
        kode = kode.strip().upper()
        if not kode:
            raise ValueError("Kode alat tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong.")
        if kode in self.__data:
            raise ValueError(f"Kode alat {kode} sudah terdaftar.")
        kategori = self.__normalisasi_kategori(kategori)
        alat = Alat(kode, nama.strip(), kategori, stok)
        self.__data[kode] = alat
        return alat

    def ubah(self, kode: str, nama: str, kategori: str) -> None:
        alat = self.ambil(kode)
        if not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong.")
        alat.ubah_data(nama.strip(), self.__normalisasi_kategori(kategori))

    def hapus(self, kode: str) -> None:
        alat = self.ambil(kode)
        if not alat.bisa_dihapus():
            raise ValueError("Alat tidak dapat dihapus karena sedang dipinjam.")
        del self.__data[alat.kode]

    def ambil(self, kode: str) -> Alat:
        kode = kode.strip().upper()
        if kode not in self.__data:
            raise ValueError(f"Alat dengan kode {kode} tidak ditemukan.")
        return self.__data[kode]

    def cari(self, kata_kunci: str) -> list[Alat]:
        kunci = kata_kunci.strip().lower()
        return [a for a in self.__data.values()
                if kunci in a.kode.lower() or kunci in a.nama.lower()
                or kunci in a.kategori.lower()]

    def semua(self) -> list[Alat]:
        return list(self.__data.values())

  
    def daftar_tersedia(self) -> list[Alat]:
        return [a for a in self.__data.values() if a.stok_tersedia > 0]

    def daftar_dipinjam(self) -> list[Alat]:
        return [a for a in self.__data.values() if a.stok_dipinjam > 0]

    def daftar_rusak(self) -> list[Alat]:
        return [a for a in self.__data.values() if a.ada_rusak()]
