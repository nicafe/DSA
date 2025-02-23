from random import choice


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = choice(arr)
    
    arr_left = [x for x in arr if x < pivot]
    arr_middle = [x for x in arr if x == pivot]
    arr_right = [x for x in arr if x > pivot]
    
    return quick_sort(arr_left) + arr_middle + quick_sort(arr_right)


def merge_sort(arr):
    if len(arr) < 2:
        return arr
        
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    
    res = []
    left_pointer = 0
    right_pointer = 0
    
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1
    
    if left_pointer < len(left):
        res.extend(left[left_pointer:])
    else:
        res.extend(right[right_pointer:])
    
    return res


arr = [6, 4, 3, 7, 5, 1, 2]
print(merge_sort(arr))