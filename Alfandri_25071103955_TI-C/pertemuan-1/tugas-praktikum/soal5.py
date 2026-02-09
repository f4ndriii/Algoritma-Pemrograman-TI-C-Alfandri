#Membuat fungsi yang menerima 2 parameter dan mengembalikan hasil penjumlahan dan pengurangan
#Serta menampilkannya

def hitung(a, b):
    return a + b, a - b

hasil_penjumlahan, hasil_pengurangan = hitung(12, 6)

print('Penjumlahan =',hasil_penjumlahan)
print('Pengurangan =',hasil_pengurangan)