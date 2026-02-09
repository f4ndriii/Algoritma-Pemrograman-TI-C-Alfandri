def penambahan (a, b):
    return a + b

def pengurangan (a, b):
    return a - b

def perkalian (a, b):
    return a * b

def pembagian (a, b):
    return a / b

def modulus (a, b):
    return a % b

def fibonacci (n):
    pass


#
n = 9
def fibonacci_correct (n):
    if n <= 1:
        return n
    else:
        return fibonacci_correct(n - 1) + fibonacci_correct(n - 2)

for i in range(n):
    print(fibonacci_correct(i))