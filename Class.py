class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __str__(self):
        return(f"Nama: {self.nama}, NIM: {self.nim}")

class Atk:
    def __init__(self, alat, jumlah):
        self.alat = alat
        self.jumlah = jumlah
        
    def __str__(self):
        return(f"Nama Alat: {self.alat}, Jumlah: {self.jumlah}")

mhs1 = Mahasiswa("Andi", "123")
atk1 = Atk("Pulpen", "1")

print(mhs1)
print(atk1)
# print(mhs1.nama)
# print(mhs1.nim)