struktur = {
    "Skripsi_Aku": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def hitung_total_ukuran(data):
    total = 0
    for i in data.values():
        if isinstance(i, dict):
            total += hitung_total_ukuran(i)
        if isinstance(i, int):
            total += i
    return total

def hitung_banyak_file(data):
    total = 0
    for i in data.values():
        if isinstance(i, dict):
            total += hitung_banyak_file(i)
        if isinstance(i, int):
            total += 1
    return total

def cari_terbesar(data):
    terbesar = 0
    for i in data.values():
        if isinstance(i, int):
            if i > terbesar:
                terbesar = i
        elif isinstance(i, dict):
            terbesar = cari_terbesar(i)
    return terbesar

def cetak(data, target=None, level=0):
    for key, value in data.items():
        if isinstance(value, dict):
            if target is None or key == target:
                if level == 0:
                    print(key)
                else:
                    print(" " * level, key)
                cetak(value, target=None, level = level + 2)
            else:
                cetak(value, target, level)
        elif isinstance(value, int):
            if target is None:
                print(" " * level, key)

print("Total ukuran skripsi:", hitung_total_ukuran(struktur))
print("Jumlah file:", hitung_banyak_file(struktur))
print("File Terbesar:", cari_terbesar(struktur))
print("")
cetak(struktur)
print("")
cetak(struktur, "Bab_3")