'''
1. Tentukan jumlah minggu (baris) dan jumlah kategori buku (kolom) melalui input
pengguna.
2. Gunakan nested for loop untuk menginput jumlah buku dipinjam pada setiap minggu
untuk setiap kategori.
3. Tampilkan matriks data peminjaman dalam format tabel yang rapi.
4. Hitung dan tampilkan:
• total peminjaman per minggu (jumlah tiap baris) dan
• total peminjaman per kategori (jumlah tiap kolom).
'''

minggu = int(input(f"{"Masukkan jumlah minggu":<33}: "))
kategori = int(input(f"{"Masukkan jumlah kategori buku":<33}: "))

matriks = []

for baris in range(minggu):
    baris_matriks = []
    print(f"\n>>> Jumlah Buku yang Dipinjam di minggu ke-{baris + 1} <<<")
    for elemen in range(kategori):
        baris_matriks.append(int(input(f"Kategori {elemen + 1}: ")))
    matriks.append(baris_matriks)

print("\n")

# Hitung jumlah buku per minggu
per_minggu = []
for baris in matriks:
    jumlah = 0
    for elemen in baris:
        jumlah += elemen
    per_minggu.append(jumlah)

# Hitung jumlah buku per kategori
per_kategori = []
for index in range(kategori):
    jumlah = 0
    for baris in matriks:
        jumlah += baris[index]
    per_kategori.append(jumlah)

print(f"{"":<23}", end=" ")
for i in range(kategori):
    print(f"Kategori ke-{i+1}{"":<5}", end=" ")
print(f"Jumlah per minggu")
print("-"*(18*kategori+43))

minggu_header = 1
index_per_minggu = 0
for baris in matriks:
    print(f"minggu ke-{minggu_header:<11}{"|":<2}", end=" ")
    for elemen in baris:
        print(f"{elemen:<18}", end=" ")
    if index_per_minggu < minggu:
        print(f"{per_minggu[index_per_minggu]}")
        index_per_minggu += 1
    minggu_header += 1

print(f"{"jumlah per kategori":<21}{"|":<2}", end=" ")

for jumlah in per_kategori:
    print(f"{jumlah:<18}", end=" ")
print("")