#Python Function
#Creating a Function

def my_function():
    print("Hello from a function")

my_function() #memanggil fungsi dan bisa dipanggil berkali-kali

#Return Values
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

#Pass statement sama seperti sebelumnya



#Python Argument
def my_function(fname):         #fname adalah parameter
    print(fname + " Refsnes")

my_function("Emil")             #"Emil" adalah argumen
my_function("Tobias")           #"Tobias" adalah argumen
my_function("Linus")            #"Linus" adalah argumen

#Default Parameter Values
#bisa menmbahkan default value ke parameter jika fungsi dipanggil tanpa argumen
def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword Arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
#bisa mengirim arguman dengan menentukan nama parameter
#jika menggunakan cara ini urutan argumen tidak lagi penting
#jika tanpa menyebutkan nama parameter urutan argumen menjadi penting
#juga bisa dicampur
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
my_function("dog", age = 5, name = "Buddy")

#Passing Different Data Types
#tipe data ditentukan saat function dijalankan, jadi bebas tipe data dalam argumen
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Sending a dictionary as an argument:
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#Return Values
#kurang lebih sama seperti bahasa C

#Returning Different Data Types

#function that returns a list
def my_function():
    return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#function that returns a tuple
def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Positional-Only Arguments
#argumen tidak bisa menggunakan keyword, hanya bisa berdasar posisi
def my_function(name, /):
    print("Hello", name)
my_function("Emil")

#Keyword-Only Argument
#Kebalikan dari yang sebelumnya
def my_function(*, name):
    print("Hello", name)

my_function(name = "Emil")



#Python *args and **kwargs
#Arbitrary Arguments (*args)
#digunakan jika tidak tahu berapa banyak argumen
def jumlahkan(*angka):         # *args menampung banyak argumen
    print(angka)               # disimpan sebagai tuple

#Arbitrary Keyword Arguments (**kwargs)
# **kwargs menampung argumen berbentuk key=value
#disimpan sebagai dictionary
#contoh
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")
