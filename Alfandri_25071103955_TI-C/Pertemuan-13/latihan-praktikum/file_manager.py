import os
list_files = [f for f in os.listdir() if f.endswith(".txt")]

def tampilkan_menu():
    print("============================")
    print("PYTHON FILE MANAGER v1.0")
    print("============================")
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")
    print("------------------------------\n")

def menu():
    while True:
        tampilkan_menu()

        try:
            pilihan = int(input("Pilih menu: "))
            match pilihan:
                case 1:
                    read()
                case 2:
                    write()
                case 3:
                    delete()
                case 0:
                    print("\nKeluar dari program...")
                    break
                case _:
                    print("Masukkan pilihan yang valid...\n")
        except ValueError:
            print("Masukkan pilihan yang valid...\n")

def tampilkan_file(files=list_files):
    print("\nFile tersedia:")
    for i, j in enumerate(files, 1):
        print(f"{i}. {j}")

def read(files=list_files):
    if not files:
        print("Tidak ada file .txt ditemukan.")
        return
    tampilkan_file()
    print("")
    pilih_file = int(input("Pilih file: "))

    for i, j in enumerate(files):
        if pilih_file - 1 == i:
            with open(j) as f:
                print("\nisi file:")
                print(f"{f.read()}\n")
                return
    print("Pilihan tidak valid...\n")

def write(files=list_files):
    tampilkan_file()
    pilih_file = (input("\nPilih file/buat file baru: "))
    nomor_file = [str(i+1) for i in range(len(files))]

    # Overwrite file yang suaah ada
    if pilih_file in nomor_file:
        print("\nSilakan isi:\n")
        isi = input()
        print("")
        with open(files[int(pilih_file)-1], "w") as f:
            f.write(isi)

    # Buat file baru
    else:
        f = open(pilih_file+".txt", "x")
        list_files.append(pilih_file+".txt")
        print(f"File {pilih_file+'.txt'} berhasil dibuat...\n")

def delete(files=list_files):
    if not files:
        print("Tidak ada file .txt ditemukan.")
        return
    tampilkan_file()
    pilih_file = (input("\nPilih file yang ingin dihapus: "))
    nomor_file = [str(i+1) for i in range(len(files))]

    if pilih_file in nomor_file:
        konfirmasi = (input(f"\nYakin hapus {files[int(pilih_file)-1]} (y/n): ")).lower()

        match konfirmasi:
            case "y":
                os.remove(files[int(pilih_file)-1])
                list_files.pop(int(pilih_file)-1)
                print("File berhasil dihapus..\n")
            case "n":
                print("Penghapusan dibatalkan...\n")
    elif pilih_file not in nomor_file:
        print("Pilihan tidak valid...\n")
menu()
