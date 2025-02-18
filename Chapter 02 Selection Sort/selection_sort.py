from time import time
from random import randint

def find_index_of_smallest(arr):
    idx = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i
    return idx


def selection_sort1(arr):
    for i in range(len(arr) - 1):
        idx = find_index_of_smallest(arr[i:])
        arr[i], arr[i + idx] = arr[i + idx], arr[i]
    return arr


def selection_sort2(arr):
    for i in range(len(arr) - 1):
        idx = i
        smallest = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr


def selection_sort3(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] >= arr[j]:
                break
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                flag = False
        if flag:
            break
    return arr


def bubble_sort2(arr):
    # The difference from bubble_sort is bubbling the max value each time.
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break
    return arr
    

# print(selection_sort1([5, 3, 6, 2, 10, 3]))
# print(selection_sort2([5, 3, 6, 2, 10, 3]))
# print(selection_sort3([5, 3, 6, 2, 10, 3]))
# print(insertion_sort([5, 3, 6, 2, 10, 3]))
# print(bubble_sort([5, 3, 6, 2, 10, 3]))
# print(bubble_sort2([5, 3, 6, 2, 10, 3]))

arr1 = [randint(1, 10000) for x in range(10000)]
arr2 = list(arr1)
arr3 = list(arr1)

start = time()
selection_sort2(arr1)
print(time() - start)

start = time()
insertion_sort(arr2)
print(time() - start)

start = time()
bubble_sort(arr3)
print(time() - start)
