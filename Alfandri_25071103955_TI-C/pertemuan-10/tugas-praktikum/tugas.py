data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

print("Sebelum sort")
print(data)

def radix_sort(data):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(data)
    exp = 1

    while maxVal // exp > 0:

        while len(data) > 0:
            val = data.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                data.append(val)

        exp *= 10

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("\nsesudah radix sort")
radix_sort(data)
print(data)
print("\nsesudah merge sort")
merge_sort = mergeSort(data)
print(merge_sort)

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

angka_cari = int(input("\nMasukkan angka yang dicari: "))

hasil_linear_search = linearSearch(data, angka_cari)
if hasil_linear_search != -1:
    print(f"\nDitemukan (linear)\nindeks {hasil_linear_search} dengan nilai {data[hasil_linear_search]}\n")
else:
    print("tidak ada\n")

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return mid
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1

hasil_binary_search = binarySearch(data, angka_cari)
if hasil_binary_search != -1:
    print(f"\nDitemukan (binary)\nindeks {hasil_binary_search} dengan nilai {data[hasil_binary_search]}\n")
else:
    print("\ntidak ada\n")