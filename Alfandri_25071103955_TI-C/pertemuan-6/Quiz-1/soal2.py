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
        pinjam.append(buku_pinjam)
    elif pilihan == 0:
        break
    else:
        print("\nPilihan tidak valid...")

print("\n=== Buku yang dipinjam ===")
for i in pinjam:
    print(f"{i[0]}")

print("\n=== Jika semua buku terlambat 1 hari ===")
total_denda = 0
for i in pinjam:
    total_denda += i[1]
print(f"Total denda: {total_denda:,}")

