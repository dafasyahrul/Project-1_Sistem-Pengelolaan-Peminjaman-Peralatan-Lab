MAKS_TRANSAKSI_AKTIF = 2

class Mahasiswa:
    def __init__(self, nim: str, nama: str, no_hp: str):
        self.__nim = nim
        self.__nama = nama
        self.__no_hp = no_hp
        self.__transaksi_aktif: list[str] = []  # daftar ID transaksi aktif

    @property
    def nim(self) -> str:
        return self.__nim

    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def no_hp(self) -> str:
        return self.__no_hp

    @property
    def transaksi_aktif(self) -> list[str]:
        return list(self.__transaksi_aktif)

    def punya_transaksi_aktif(self) -> bool:
        return len(self.__transaksi_aktif) > 0

    def bisa_meminjam(self) -> bool:
        return len(self.__transaksi_aktif) < MAKS_TRANSAKSI_AKTIF

    def tambah_transaksi_aktif(self, id_trx: str) -> None:
        if not self.bisa_meminjam():
            raise ValueError(
                f"Mahasiswa {self.__nim} sudah mencapai batas "
                f"{MAKS_TRANSAKSI_AKTIF} transaksi aktif."
            )
        if id_trx not in self.__transaksi_aktif:
            self.__transaksi_aktif.append(id_trx)

    def hapus_transaksi_aktif(self, id_trx: str) -> None:
        if id_trx in self.__transaksi_aktif:
            self.__transaksi_aktif.remove(id_trx)

    def ubah_data(self, nama: str, no_hp: str) -> None:
        self.__nama = nama
        self.__no_hp = no_hp

    def __str__(self) -> str:
        return (f"NIM: {self.__nim} | Nama: {self.__nama} | "
                f"No HP: {self.__no_hp} | "
                f"Transaksi aktif: {len(self.__transaksi_aktif)}")
