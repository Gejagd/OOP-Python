class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")


mhs1 = Mahasiswa("Andi", "123")
mhs1.tampilkan_data()
# print(mhs1.nama)
# print(mhs1.nim)