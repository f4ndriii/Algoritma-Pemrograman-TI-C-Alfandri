def pangkat_rekursif(a, b):
    if b == 1:
        return a
    elif b > 1:
        return a * pangkat_rekursif(a, b - 1)

print(pangkat_rekursif(2, 5))