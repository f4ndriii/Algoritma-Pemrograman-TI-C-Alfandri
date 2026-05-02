'''
1. Buat list buku berisi 5 item buku beserta denda per hari keterlambatan, contoh:
[["Algoritma", 2000], ["Basis Data", 2500], ...].
2. Tampilkan seluruh daftar buku beserta denda menggunakan for loop dengan penomoran.
3. Minta pengguna memasukkan nomor buku yang dipilih.
4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error;
jika valid, tampilkan judul buku dan denda per hari.
'''

buku = [
    ["Matematika", 5000],
    ["Fisika", 3000],
    ["Kimia", 2000],
    ["Sejarah", 4000],
    ["Bahasa Inggris", 6000]
]

for x in buku:
    print(f"{buku.index(x)+1}. Nama Buku: {x[0]:<18} Denda: {x[1]}")

pilihan = int(input("\nMasukkan pilihan: "))

if pilihan <= len(buku) and pilihan > 0:
    print(f"\n{"Buku yang dipinjam":<24} : {buku[pilihan-1][0]}")
    print(f"{"Denda keterlambatan":<24} : {buku[pilihan-1][1]}")
else:
    print("\nPilihan tidal valid...")