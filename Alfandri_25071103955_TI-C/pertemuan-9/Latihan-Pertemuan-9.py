'''
Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu Insertion Sort , Quick Sort dan Counting Sort secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
Implementasikan fungsi terpisah untuk 

Insertion Sort , Quick Sort dan Counting Sort.
Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
'''

def insertion_sort(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array.pop(i)
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                insert_index = j
        my_array.insert(insert_index, current_value)
    return my_array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)

def countingSort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr

while True:
    jumlah_elemen = int(input(f"Masukkan jumlah elemen: "))

    if jumlah_elemen <= 0:
        print("Jumlah elemen tidak boleh nol atau kecil dari nol\n")
    else:
        break

array = []

i = 0
while True:
    temp = int(input(f"Masukkan elemen ke {i+1}: "))

    if temp >= 0:
        array.append(temp)
        i+=1
        if len(array) == jumlah_elemen:
            break
    else:
        print("Tidak boleh negatif\n")

print(f"\nInsertion sort\n{insertion_sort(array)}\n")

print(f"Counting sort\n{countingSort(array)}\n")

quicksort(array)
print("Quick sort")
print(array)