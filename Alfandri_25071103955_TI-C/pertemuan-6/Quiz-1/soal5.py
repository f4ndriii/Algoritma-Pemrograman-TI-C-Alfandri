'''
1. Buat class Buku dengan atribut judul dan denda_per_hari, serta method tampilkan() yang
mencetak informasi buku dalam format: "Judul Buku - Denda Rp .../hari".
2. Buat class Peminjaman dengan atribut total_denda (awalnya 0) dan method
tambah(buku, hari_terlambat) untuk menambahkan denda ke total, serta method
ringkasan() untuk menampilkan total denda.
3. Pada program utama, buat minimal 3 objek Buku dan tampilkan semuanya menggunakan
for loop.
4. Buat satu objek Peminjaman, minta pengguna memilih buku dan input hari
keterlambatan, lalu panggil method tambah() dan tampilkan ringkasan akhir dengan
method ringkasan().
'''

class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari

    def tampilkan(self):
        print(f"{self.judul} - Denda Rp{self.denda_per_hari}/hari")

class Peminjaman:
    def __init__(self):
        self.total_denda = 0

    def tambah(self, buku, hari_terlambat):
        denda_tambahan = buku.denda_per_hari * hari_terlambat
        self.total_denda += denda_tambahan
        print(f">Berhasil menambahkan denda untuk buku {buku.judul} selama {hari_terlambat} hari.")

    def ringkasan(self):
        print(f"Total denda: {self.total_denda}")

daftar_buku = [
    Buku("Meditation", 2000),
    Buku("Bumi Manusia", 3000),
    Buku("Filosofi Teras", 2500)
]

for i, j in enumerate(daftar_buku, 1):
    print(f"{i}. ", end="")
    j.tampilkan()

pinjam = Peminjaman()

try:
    pilihan = int(input("\nSilakan pilih: ")) - 1
    if 0 <= pilihan < len(daftar_buku):
        hari_terlambat = int(input("Berapa hari keterlambatan: "))
        if hari_terlambat < 0:
            print(f"Hari terlambat tidak boleh kecil dari nol...")
        else:
            pinjam.tambah(daftar_buku[pilihan], hari_terlambat)
            pinjam.ringkasan()
except ValueError:
    print(f"Masukkan angka yang valid...")