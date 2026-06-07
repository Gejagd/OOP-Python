class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __str__(self):
        return(f"Nama: {self.nama}, NIM: {self.nim}")

mhs1 = Mahasiswa("Andi", "123")
print(mhs1)
# print(mhs1.nama)
# print(mhs1.nim)