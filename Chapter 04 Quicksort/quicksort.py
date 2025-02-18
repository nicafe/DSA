from time import time
from random import randint


def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)



# quicksort() is clearer, but quicksort2() performs better.
def quicksort2(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    
    res = quicksort(less)
    res.append(pivot)
    res.extend(greater)
    return res
    

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
        # the same as res += arr1[pointer1:]
        # better than res = res + arr1[pointer1:]
    else:
        res.extend(arr2[pointer2:])
    return res



# print(quicksort([5, 3, 6, 2, 10, 3]))
# print(quicksort2([5, 3, 6, 2, 10, 3]))
# print(merge_sort([5, 3, 6, 2, 10, 3]))

arr1 = [randint(1, 10000) for x in range(10000)]
arr2 = list(arr1)
start = time()
quicksort(arr1)
print(time() - start)
start = time()
quicksort2(arr2)
print(time() - start)
