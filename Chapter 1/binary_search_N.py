# Two-pointer method in the book.
def binary_search_two_pointer(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Recursion.
def binary_search_recursion(lst, item):
    if lst == []:
        return None
    
    mid = len(lst) // 2
    guess = lst[mid]
    if guess == item:
        return mid
    if guess > item:
        return binary_search_recursion(lst[:mid], item)
    res = binary_search_recursion(lst[mid + 1:], item)
    return None if res is None else mid + 1 + res


# The iteration corresponding to recursion.
def binary_search_iter(lst, item):
    idx = 0
    while lst != []:
        mid = len(lst) // 2
        guess = lst[mid]
        if guess == item:
            return idx + mid
        if guess > item:
            lst = lst[:mid]
        else:
            lst = lst[mid + 1:]
            idx += mid + 1
    return None


LIST = [1, 3, 6, 7, 10, 13, 15, 18, 20, 21, 22]
idx = binary_search_two_pointer(LIST, 6)
print(idx)
