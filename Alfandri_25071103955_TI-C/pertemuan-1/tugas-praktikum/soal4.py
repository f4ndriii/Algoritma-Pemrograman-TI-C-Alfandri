#Membuat program python yang menampilkan angka 1-10 menggunakan for loop
#Dan menghitung jumlah 1-10 serta menampilkannya

jumlah = 0
for angka in range(1, 11):
    print(angka)
    jumlah+= angka
print('Jumlah =',jumlah)