def bilangan_prima(n):
    list_bilangan_prima = []
    for x in range(n):
        faktor_pembagi = 0
        for y in range(x):
            if x % (y + 1) == 0:
                faktor_pembagi += 1
        if faktor_pembagi == 2:
            list_bilangan_prima.append(x)
    return list_bilangan_prima

list1 = bilangan_prima(50)
print(list1)