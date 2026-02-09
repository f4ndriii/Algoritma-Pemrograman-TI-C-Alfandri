#Python_Numbers

#ada 3 tipe data numerik: integer, float, dan complex

#integer/bilangan bulat
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#float/bilangan desimal
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#float juga bisa berupa angka ilmiah dengan huruf "e" 
#untuk menunjukkan pangkat 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))



#Koneversi_Tipe
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert dari int ke float:
a = float(x)

#convert dari float ke int:
b = int(y)

#convert dari int ke complex:
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))



#Random_Numbers
#Python tidak memiliki fungsi random() untuk membuat angka acak,
#tetapi Python memiliki modul bawaan bernama random
#yang dapat digunakan untuk membuat angka acak:
import random
print(random.randrange(1, 10))