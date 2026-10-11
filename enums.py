from enum import Enum

class KondisiAlat(Enum):
    BAIK = "BAIK"
    RUSAK_RINGAN = "RUSAK_RINGAN"
    RUSAK_BERAT = "RUSAK_BERAT"

class StatusTransaksi(Enum):
    DIPINJAM = "DIPINJAM"
    SEBAGIAN_DIKEMBALIKAN = "SEBAGIAN_DIKEMBALIKAN"
    SELESAI = "SELESAI"
