#Boolean_Values
#boolean value terdiri dari 2 yaitu true/false

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Evaluate_Values_and_Variables
#Fungsi bool() memungkinkan untuk mengevaluasi nilai apa pun,
#dan memberikan nilai True atau False sebagai hasilnya.

print(bool("Hello"))
print(bool(15))

#Most_Values_are_True
#semua string nilainya true kecuali string kosong
#semua angka nilainya true kecuali 0
#semua list, tuple, set, dan dictionary nilainya true kecuali yang kosong

#Some_Values_are_False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Functions_can_Return_Boolean
def myFunction() :
    return True
print(myFunction())

#bisa juga eksekusi kode berdasarkan nilai boolean dari suatu fungsi
def myFunction() :
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")

#menegcek apakah objek integer
x = 200
print(isinstance(x, int))