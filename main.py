import random
from datetime import datetime


def insertionSort1(arr1):
    now1 = datetime.now()
    for i in range(1, len(arr1)):

        key = arr1[i]

        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key

    now2 = datetime.now()
    print("zajęło to")
    print(now2 - now1)


def insertionSort2(arr1):
    now1 = datetime.now()
    for i in range(1, len(arr1)):

        key = arr1[i]

        j = i - 1
        while j >= 0 and key > arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key

    now2 = datetime.now()
    print("zajęło to")
    print(now2 - now1)


def selectionSort1(arr2):
    now1 = datetime.now()
    for i in range(len(arr2)):
        min_idx = i

        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr[j]:
                min_idx = j

        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
    now2 = datetime.now()
    print("ile to zajęło")
    print(now2 - now1)


def selectionSort2(arr2):
    now1 = datetime.now()
    for i in range(len(arr2)):
        min_idx = i

        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] < arr[j]:
                min_idx = j

        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
    now2 = datetime.now()
    print("ile to zajęło")
    print(now2 - now1)


def mergeSort1(arr3):
    if len(arr3) > 1:

        mid = len(arr3) // 2

        L = arr3[:mid]

        R = arr3[mid:]

        mergeSort1(L)

        mergeSort1(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr3[k] = L[i]
                i += 1
            else:
                arr3[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr3[k] = R[j]
            j += 1
            k += 1


def mergeSort2(arr3):
    if len(arr3) > 1:

        mid = len(arr3) // 2

        L = arr3[:mid]

        R = arr3[mid:]

        mergeSort2(L)

        mergeSort2(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr3[k] = L[i]
                i += 1
            else:
                arr3[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr3[k] = R[j]
            j += 1
            k += 1


print("dodanie liczb do tableli")
arr = [random.randint(-1000000000, 1000000000) for i in range(50000)]
arr1 = arr
arr2 = arr
arr3 = arr



print("---selection sort---")

print("sortowanie od najmniejszego")
selectionSort1(arr1)

print("sortowanie od największego")
selectionSort2(arr1)

print("---insertion sort---")

print("sortowanie od najmniejszego")
insertionSort1(arr2)

print("sortowanie od największego")
insertionSort1(arr2)

print("---merge sort---")

now1 = datetime.now()
print("sortowanie od najmniejszego")
mergeSort1(arr3)
now2 = datetime.now()
now3 = now2 - now1
print("zajęło to:")
print(now3)

print("sortowanie od największego")
now1 = datetime.now()
mergeSort2(arr3)
now2 = datetime.now()
print("zajęło to:")
print(now3)

print("Dodanie do tabeli nieposotrowanych liczb losowych")
arr.extend(random.randint(-1000000000, 1000000000) for j in range(50000))
arr2 = arr
arr3 = arr
print("---insertion sort---")
insertionSort1(arr2)


print("---merge sort---")
print("sortowanie on najmniejszego ")
now1 = datetime.now()
mergeSort1(arr3)
now2 = datetime.now()
now3 = now2 - now1
print("zajęło to:")
print(now3)
