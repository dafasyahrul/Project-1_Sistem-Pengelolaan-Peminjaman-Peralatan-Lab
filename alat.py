"""Kelas entitas Alat (stok dikelola per kondisi)."""
from models.enums import KondisiAlat


class Alat:
    def __init__(self, kode: str, nama: str, kategori: str, stok_total: int):
        if stok_total < 1:
            raise ValueError("Stok harus minimal 1.")
        self.__kode = kode
        self.__nama = nama
        self.__kategori = kategori
        self.__stok_total = stok_total
        self.__stok_tersedia = stok_total
        self.__stok_dipinjam = 0
        self.__stok_rusak_ringan = 0
        self.__stok_rusak_berat = 0

    # ---- getter ----
    @property
    def kode(self) -> str:
        return self.__kode

    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def kategori(self) -> str:
        return self.__kategori

    @property
    def stok_total(self) -> int:
        return self.__stok_total

    @property
    def stok_tersedia(self) -> int:
        return self.__stok_tersedia

    @property
    def stok_dipinjam(self) -> int:
        return self.__stok_dipinjam

    @property
    def stok_rusak_ringan(self) -> int:
        return self.__stok_rusak_ringan

    @property
    def stok_rusak_berat(self) -> int:
        return self.__stok_rusak_berat

    # ---- perilaku ----
    def ubah_data(self, nama: str, kategori: str) -> None:
        self.__nama = nama
        self.__kategori = kategori

    def cukup_stok(self, jumlah: int) -> bool:
        return 0 < jumlah <= self.__stok_tersedia

    def keluarkan_untuk_dipinjam(self, jumlah: int) -> None:
        if not self.cukup_stok(jumlah):
            raise ValueError(
                f"Stok '{self.__nama}' tidak cukup "
                f"(diminta {jumlah}, tersedia {self.__stok_tersedia})."
            )
        self.__stok_tersedia -= jumlah
        self.__stok_dipinjam += jumlah

    def terima_kembali(self, jumlah: int, kondisi: KondisiAlat) -> None:
        if jumlah < 1 or jumlah > self.__stok_dipinjam:
            raise ValueError(
                f"Jumlah kembali tidak valid untuk '{self.__nama}' "
                f"(sedang dipinjam {self.__stok_dipinjam})."
            )
        self.__stok_dipinjam -= jumlah
        if kondisi == KondisiAlat.BAIK:
            self.__stok_tersedia += jumlah
        elif kondisi == KondisiAlat.RUSAK_RINGAN:
            self.__stok_rusak_ringan += jumlah
        else:
            self.__stok_rusak_berat += jumlah

    def bisa_dihapus(self) -> bool:
        return self.__stok_dipinjam == 0

    def ada_rusak(self) -> bool:
        return (self.__stok_rusak_ringan + self.__stok_rusak_berat) > 0

    def __str__(self) -> str:
        return (f"[{self.__kode}] {self.__nama} ({self.__kategori}) | "
                f"Total: {self.__stok_total} | Tersedia: {self.__stok_tersedia} | "
                f"Dipinjam: {self.__stok_dipinjam} | "
                f"Rusak ringan: {self.__stok_rusak_ringan} | "
                f"Rusak berat: {self.__stok_rusak_berat}")
