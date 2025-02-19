import random
import time

def test_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def test_algorithm(func, arr):
    start_time = time.time()
    sorted_array = func(arr)
    end_time = time.time()
    print("Algorithm:", func.__name__)
    print("Sorted:", len(sorted_array) == len(arr) and test_sorted(sorted_array))
    print("Time:", end_time - start_time)
    print()
    return sorted_array

def selection_sort(arr):
    arr = list(arr)
    sort_index = 0
    while sort_index < len(arr):
        min_index = sort_index
        for i in range(sort_index + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[sort_index], arr[min_index] = arr[min_index], arr[sort_index]
        sort_index += 1
    return arr

def insertion_sort(arr):
    arr = list(arr)
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def merge(arr1, arr2):
    index1 = 0
    index2 = 0
    result = []
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            result.append(arr1[index1])
            index1 +=1
        else:
            result.append(arr2[index2])
            index2 +=1
    result.extend(arr1[index1:])
    result.extend(arr2[index2:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_index = int(len(arr) / 2)
    return merge(merge_sort(arr[:mid_index]), merge_sort(arr[mid_index:]))

def quick_sort_zero(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    arr_left = []
    arr_right = []
    for i in arr[1:]:
        if i < pivot:
            arr_left.append(i)
        elif i >= pivot:
            arr_right.append(i)
    return quick_sort_zero(arr_left) + [pivot] + quick_sort_zero(arr_right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr_left = [x for x in arr if x < pivot]
    arr_middle = [x for x in arr if x == pivot]
    arr_right = [x for x in arr if x > pivot]
    return quick_sort(arr_left) + arr_middle + quick_sort(arr_right)

# --- Testing ---

l = 10000
random_array = [random.randint(0, l - 1) for _ in range(l)]
ordered_array = list(range(l))

print("--- Random Array ---\n")
test_algorithm(selection_sort, random_array)
test_algorithm(insertion_sort, random_array)
test_algorithm(merge_sort, random_array)
test_algorithm(quick_sort_zero, random_array)
test_algorithm(quick_sort, random_array)

print("--- Ordered Array ---\n")
test_algorithm(selection_sort, ordered_array)
test_algorithm(insertion_sort, ordered_array)
test_algorithm(merge_sort, ordered_array)
# test_algorithm(quick_sort_zero, ordered_array)
test_algorithm(quick_sort, ordered_array)

# print("Validity:", test_sorted(random_array) == False)

