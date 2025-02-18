from time import time
from random import randint


def find_index(arr, target=None):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def selection_sort1(arr):
    res = []
    while arr != []:
        index = find_index(arr, min(arr))
        res.append(arr[index])
        arr.pop(index)
    return res


def selection_sort2(arr):
    for i in range(len(arr) - 1):
        idx = 0
        new_arr = arr[i:]
        smallest = new_arr[0]
        for j in range(1, len(new_arr)):
            if new_arr[j] < smallest:
                smallest = new_arr[j]
                idx = j
        arr[i], arr[i + idx] = arr[i + idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] > arr[j]:
                break
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                flag = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag:
            break
    return arr


arr1 = []
for i in range(10000):
    arr1.append(randint(1, 10000))
    
arr2 = list(arr1)

start = time()
selection_sort1(arr1)
end = time()
print(end - start)

start = time()
selection_sort2(arr2)
end = time()
print(end - start)