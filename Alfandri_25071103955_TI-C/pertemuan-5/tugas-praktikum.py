A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

#a
def jumlah(matriks1, matriks2):
    baris, kolom = len(matriks1), len(matriks1[0])
    hasil = [[matriks1[i][j] + matriks2[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

C_tambah = jumlah(A, B)



#b
def kurang(matriks1, matriks2):
    baris, kolom = len(matriks1), len(matriks1[0])
    hasil = [[matriks1[i][j] - matriks2[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

C_kurang = kurang(A, B)



#c
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

C_skalar = kali_skalar(A, 4)



#d
def determinan_3x3(matriks):
    d1 = matriks[0][0] * matriks[1][1] * matriks[2][2]
    d2 = matriks[0][1] * matriks[1][2] * matriks[2][0]
    d3 = matriks[0][2] * matriks[1][0] * matriks[2][1]
    d4 = matriks[0][2] * matriks[1][1] * matriks[2][0]
    d5 = matriks[0][0] * matriks[1][2] * matriks[2][1]
    d6 = matriks[0][1] * matriks[1][0] * matriks[2][2]
    return (d1 + d2 + d3) - (d4 + d5 + d6)

det_A = determinan_3x3(A)
det_B = determinan_3x3(B)



#e
print("Hasil tambah")
for i in C_tambah:
    print(i)
print("\nHasil kurang")
for i in C_kurang:
    print(i)
print("\nHasil kali skalar")
for i in C_skalar:
    print(i)
print("\ndet(A)")
print(det_A)
print("\ndet(B)")
print(det_B)