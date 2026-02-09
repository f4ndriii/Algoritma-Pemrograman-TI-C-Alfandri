#Python_Strings

#String

#string di python bisa menggunakan single atau double quote
print("Hello")
print('Hello')

#Quotes_Inside_Quotes

#Jika ingin menggunakan kutipan dalam string
#maka kutipan yang di dalam string harus berbeda dengan 
#kutipan yang mengurung string 
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign_String_to_a_Variable

#cukup dengan menuliskan nama variabel dan diikuti sama dengan dan stringnya
a = "Hello"
print(a)

#Multiline_Strings

#bisa dengan menggunakan triple quote (single/double)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings_are_Arrays

#sama seperti bahasa C di python string juga merupakan array yang elemennya bisa kita akses
a = "Hello, World!"
print(a[1])

#Looping_Through_a_String

#karena string juga merupakan array, maka kita bisa melakukan looping dengan elemennya
for x in "banana":
    print(x)

#String_Length

#untuk mengetahui panjang string
a = "Hello, World!"
print(len(a))

#Check_String

#untuk memeriksa apakah frasa atau karakter tertentu ada dalam
#sebuah string

txt = "The best things in life are mie ayam!"
print("mie ayam" in txt)

#bisa digunakan dengan if juga
txt = "The best things in life are mie ayam!"
if "mie ayam" in txt:
    print("Yes, 'mie ayam' is present.")

#Check_if_NOTUntuk memeriksa apakah frasa atau karakter tertentu
#TIDAK ada dalam sebuah string,
#kita dapat menggunakan kata kunci `not in`

txt = "The best things in life are free!"
print("expensive" not in txt)



#Slicing_strings

#Slicing
#menampilkan karakter dalam rentang tertentu
b = "Hello, World!"
print(b[2:5])

#Slicing_from_start
#menampilkan karakater dari awal sampai posisi yang ditentuka
b = "Hello, World!"
print(b[:5])

#Slice_to_The_End
#menampilkan karakter dari posisi yang ditentukan sampai berakhir
b = "Hello, World!"
print(b[2:])

#Negative_Indexing
#memotong string dari belakang
b = "Hello, World!"
print(b[-5:-2])



#Modify_strings

#Upper_Case
#mengubah string menjadi huruf kapital
a = "Hello, World!"
print(a.upper())

#Lower_Case
#mengubah string menjadi huruf kecil
a = "Hello, World!"
print(a.lower())

#Remove_Whitespace
#menghapus whitespace dari awal
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace_String
#menggnati suatu huruf dengan huruf lain
a = "Hello, World!"
print(a.replace("H", "J"))

#Split_String
#membagai sebuah string menjadi beberapa bagian
#(,) berfungsi sebagai pemisah
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

