'''
1. Minta pengguna menginput jumlah hari keterlambatan.
2. Gunakan while loop untuk memastikan hari keterlambatan tidak kurang dari 0. Jika < 0,
tampilkan pesan error dan minta input ulang.
3. Hitung total denda berdasarkan buku yang dipinjam dan hari keterlambatan.
• Gunakan if-else untuk menampilkan pesan:
• "Tidak ada denda" jika hari keterlambatan = 0, atau
• "Total denda Anda: Rp ..." jika ada keterlambatan.
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

pinjam = []
while True:
    pilihan = int(input("\nMasukkan nomor buku yang akan dipinjam(0 jika selesai): "))
    if pilihan <= len(buku) and pilihan > 0:
        buku_pinjam = []
        buku_pinjam.append(buku[pilihan-1][0])
        buku_pinjam.append(buku[pilihan-1][1])
        while True:
            buku_pinjam.append(int(input("Berapa hari keterlambatan: ")))
            if buku_pinjam[2] >= 0:
                break
            else:
                print("Input tidak valid...")
        pinjam.append(buku_pinjam)
    elif pilihan == 0:
        break
    else:
        print("\nPilihan tidak valid...")

print("\n=== Buku yang dipinjam ===")
for i in pinjam:
    print(f"{i[0]}")

print("\n=== Total denda keterlambatan ===")
total_denda = 0
for i in pinjam:
    total_denda += i[2] * i[1]
print(f"Total denda: {total_denda:,}")