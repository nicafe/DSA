def binary_search(remaining, steps=0):
    if remaining == 1:
        print(steps)
        return
    
    next_remaining = remaining / 2
    if next_remaining.is_integer():
        binary_search(int(next_remaining), steps + 1)
    else:
        binary_search(int(next_remaining) + 1, steps + 1)


# 1.1
binary_search(128)

# 1.2
binary_search(128 * 2)
