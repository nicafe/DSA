from time import time
from random import randint


def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)


def merge_sort(arr):
    if len(arr) < 2:
        return arr
        
    arr1 = merge_sort(arr[:len(arr) // 2])
    arr2 = merge_sort(arr[len(arr) // 2:])
    
    res = []
    pointer1 = pointer2 = 0
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] <= arr2[pointer2]:
            res.append(arr1[pointer1])
            pointer1 += 1
        else:
            res.append(arr2[pointer2])
            pointer2 += 1
    if pointer1 < len(arr1):
        res.extend(arr1[pointer1:])
        # list1.extend(list2) is the same as list1 += list2,
        # performs slightly better than list1 = list1 + list2.
    else:
        res.extend(arr2[pointer2:])
    return res


def counting_sort(arr, k):
    count = [0] * (k + 1)
    
    for num in arr:
        count[num] += 1
    
    res = []
    for i in range(len(count)):
        if count[i]:
            res.extend([i] * count[i])
    return res


# print(quicksort([5, 3, 6, 2, 10, 3]))
# print(merge_sort([5, 3, 6, 2, 10, 3]))
# print(counting_sort([5, 3, 6, 2, 10, 3], 10))

k = 100000
arr1 = [randint(0, k) for x in range(k)]
arr2 = list(arr1)
arr3 = list(arr1)
arr4 = list(arr1)

start = time()
quicksort(arr1)
print('Quiick:', time() - start)

start = time()
merge_sort(arr2)
print('Merge:', time() - start)

start = time()
counting_sort(arr3, k)
print('Counting:', time() - start)

start = time()
sorted(arr4)
print('Builtin:', time() - start)
