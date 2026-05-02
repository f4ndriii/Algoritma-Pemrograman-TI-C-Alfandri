DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]
riwayat = []

#A
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    """Menentukan pemenang"""
    menang = {
        "batu" : "gunting",
        "gunting" : "kertas",
        "kertas" : "batu"
    }

    if menang[pilihan_pemain] == pilihan_komputer:
        return "pemain"
    elif menang[pilihan_komputer] == pilihan_pemain:
        return "komputer"
    elif pilihan_komputer == pilihan_pemain:
        return "seri"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
        pilihan_pemain = input(f"Pilihan pemain: ").lower
        cek = ["gunting", "batu", "kertas"]
        if pilihan_pemain in cek:               #cek apakah pilihan pemain valid (batu/gunting/kertas)
            break
    hasil_giliran = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    if hasil_giliran == "pemain" or hasil_giliran == "komputer":
        print(f"Pilihan pemain: {pilihan_pemain}")
        print(f"Pilihan komputer: {pilihan_komputer}")
    print(f"Hasil: {hasil_giliran}")
    return hasil_giliran

def main_satu_ronde(nama, nomor_ronde):
    nomor_giliran = 0
    pemain_menang = 0
    komputer_menang = 0

    print(f"Ronde {nomor_ronde}")

    while pemain_menang < 3 and komputer_menang < 3:
        hasil = main_satu_giliran(nomor_giliran)
        nomor_giliran += 1
        if hasil == "pemain":
            pemain_menang += 1
        elif hasil == "komputer":
            komputer_menang += 1

        if pemain_menang >= 3:
            print(f"Pemain menang")
        elif komputer_menang >= 3:
            print(f"Komputer menang")
    skor = pemain_menang*10
    return [nama, skor]


#B
def tampilkan_riwayat(riwayat):
    if len(riwayat) == 0:
        print(f"Belum ada riwayat.")
    print(f"{"No":<3} | {"nama":<7} | {"skor":<7}")
    print("="*23)

    for i, j in enumerate(riwayat, 1):
        print(f"{"i":<3} | {j[0]:<7} | {j[1]:<7}")


#C
def bubble_sort_riwayat(riwayat):
    salinan = riwayat[:]
    n = len(salinan)

    for i in range(n):
        for j in range(n - i -1):
            if salinan[j][1] < salinan[j+1][1]:
                salinan[j][1], salinan[j+1][1] = salinan[j+1][1], salinan[j][1]
    return salinan

def tampilkan_leaderboard(riwayat):
    pass