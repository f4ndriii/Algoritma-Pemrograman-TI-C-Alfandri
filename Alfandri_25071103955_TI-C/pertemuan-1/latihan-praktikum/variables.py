#Python_Variables

#mendeklarasikan variabel tidak perlu mendeklarasikan tipe data
x = 5
y = "John"

#tipe data variabel berubah sesuai isinya
#contoh
x = 33
x = 'Ayam'
print(x)

#casting: untuk mengspesifikkan tipe data suatu variabel
a = str(5)    #hasilnya '5'
b = int(5)    #hasilnya 5
c = float(5)  #hasilnya 5.0
print(a, b, c)

#untuk mengetahui tipe data suatu variabel
print(type(a))
print(type(b))
print(type(c))

#nama variabel dengan huruf sama, cuma beda huruf kecil dan kapital berbeda
A = 'huruf besar'



#Variable_Names

#Aturan variabel python
    #nama variabel harus dimulai dari huruf atau underscore
    #nama variabel tidak boleh dimulai dari angka
    #nama variabel hanya boleh berisi alpha-numerik karakter dan underscore (A-z, 0-9, and _ )
    #nama variabel case-sensitive (aku, Aku, dan AKU tidak sama)
    #nama variabel tidak boleh berupa keyword python

#Nama variabel yang lebih dari satu kata
#ada beberapa cara penulisan
    #camelCase: setiap kata diawali huruf kapital kecuali huruf pertama
    #PascalCase: setiap kata diawali huruf kapital
    #snake_case: setiap kata dibatasi underscore



#Assign_Multiple_Values

#Many values to multiple variabel
j, k, l = 'bakso', 'gorengan', 'mangga'
print(j)
print(k)
print(l)

#One value to multiple variables
j = k = l = "mangga"
print(j)
print(k)
print(l)

#Unpack collection
angka = [1, 2, 3]
angka1, angka2, angka3 = angka
print(angka1)
print(angka2)
print(angka3)



#Output_Variables

#fungsi print bisa digunakan untuk multi variabel
print(j, k, l)
#bisa juga pakai +, tapi spasinya gak ada
print(j+k+l)



#Global_Variables

#global variabel adalah variabel yang dideklarasikan di luar fungsi
#contoh:
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
#kalau dideklarasikan didalam fungsi, variabel hanya bisa diakses di dalam fungsi

#bisa juga mendeklarasikan variabel global di dalam fungsi dengan:
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)