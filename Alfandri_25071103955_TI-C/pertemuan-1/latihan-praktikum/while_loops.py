#dengan while loop kita bisa mengeksekusi kode selama kondisi masih memenuhi
i = 1
while i < 6:
    print(i)
    i += 1

#The break Statement
#dengan break loop bisa berhenti saat kondisi masih terpenuhi
i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1

#The continue Statement
#dengan continue kita bisa stop di iterasi tertentu, lalu lanjut ke yang setelahny
i = 0
while i < 6:
    i += 1
    if i == 3:      #3 di skip
        continue
    print(i)

#The else Statement
#else statement bisa menjalankan block kode langsung setelah kondisi tidak terpenuhi lagi
#contoh
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
