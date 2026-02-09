#Operator Aritmatik

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


#Comparison operator

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#Identity Operator

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   #membandingkan alamat
print(x is y)
print(x == y)   #membandingkan isi


#Membership Operator

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise Operator

print(6 & 3)

#Operator Precedence

print((6 + 3) - (6 + 3))