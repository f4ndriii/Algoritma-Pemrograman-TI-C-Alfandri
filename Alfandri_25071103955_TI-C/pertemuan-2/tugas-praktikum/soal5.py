import math

def jarak(x1, y1, x2, y2):
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return d

hasil = jarak(0, 0, 3, 4)
print(f"Jarak = {hasil}")