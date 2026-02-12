def rata_rata(nilai):
    banyak_nilai = 0
    jumlah_nilai = 0

    if nilai:
        for x in nilai:         #Jika data berisi
            jumlah_nilai = jumlah_nilai + x
            banyak_nilai = banyak_nilai + 1
        return jumlah_nilai / banyak_nilai
    else:
        print('Data kosong')    #Jika data kosong


nilai = [80, 75, 90, 60, 85]
print(rata_rata(nilai))

nilai_kosong = []
rata_rata(nilai_kosong)

