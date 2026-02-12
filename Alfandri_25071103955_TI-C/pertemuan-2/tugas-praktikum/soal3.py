'''
def jumlah_digit(n):
    digit = [int(x) for x in str(n)]

    jumlah = 0
    for x in digit:
        jumlah += x
    return jumlah

print(jumlah_digit(1234))
'''

def jumlah_digit(n):
    if n >= 10:
        return n % 10 + jumlah_digit(n // 10)
    else:
        return n
print(jumlah_digit(1234))