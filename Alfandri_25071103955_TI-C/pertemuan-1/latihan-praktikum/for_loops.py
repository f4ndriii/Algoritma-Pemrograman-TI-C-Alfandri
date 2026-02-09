#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 

#Looping Through a String
for x in "banana":
    print(x) 

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x) 



#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x) 



#The range() Function
#untuk looping yang spesifik berapa kali pengulangan akan terjadi
#1
for x in range(6):      #default start dari 0 (6 tidak termasuk)
    print(x) 
#2
for x in range(2, 6):   #start dari 2 (6 tidak termasuk)
    print(x) 

#default kelipatan range itu satu, tapi bisa diubah
for x in range(2, 30, 3):   #kelipatan 3
    print(x) 



#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!") #ini dieksekusi setelah perulangan selesai

#jika ada break sebelum else, blok kode else tidak dijalankan

#Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement
#sama seperti while loop