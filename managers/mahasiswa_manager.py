from models.mahasiswa import Mahasiswa

class MahasiswaManager:
    def __init__(self):
        self.__data: dict[str, Mahasiswa] = {}  # key = NIM

    @staticmethod
    def _validasi(nim: str, nama: str, no_hp: str) -> None:
        if not nim or not nim.isdigit():
            raise ValueError("NIM harus berupa angka dan tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong.")
        if not no_hp.isdigit() or not (9 <= len(no_hp) <= 15):
            raise ValueError("No HP harus angka sepanjang 9-15 digit.")

    def tambah(self, nim: str, nama: str, no_hp: str) -> Mahasiswa:
        self._validasi(nim, nama, no_hp)
        if nim in self.__data:
            raise ValueError(f"NIM {nim} sudah terdaftar.")
        mhs = Mahasiswa(nim, nama.strip(), no_hp)
        self.__data[nim] = mhs
        return mhs

    def ubah(self, nim: str, nama: str, no_hp: str) -> None:
        mhs = self.ambil(nim)
        self._validasi(nim, nama, no_hp)
        mhs.ubah_data(nama.strip(), no_hp)

    def hapus(self, nim: str) -> None:
        mhs = self.ambil(nim)
        if mhs.punya_transaksi_aktif():
            raise ValueError(
                "Mahasiswa tidak dapat dihapus karena masih punya transaksi aktif.")
        del self.__data[nim]

    def cari(self, kata_kunci: str) -> list[Mahasiswa]:
        kunci = kata_kunci.strip().lower()
        return [m for m in self.__data.values()
                if kunci in m.nim.lower() or kunci in m.nama.lower()]

    def ambil(self, nim: str) -> Mahasiswa:
        if nim not in self.__data:
            raise ValueError(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        return self.__data[nim]

    def semua(self) -> list[Mahasiswa]:
        return list(self.__data.values())
