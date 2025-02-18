def counting_sort_stable(arr):
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0] * k

    for num in arr:
        count[num - min_val] += 1

    # Accumulate indexes.
    for i in range(1, k):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    # Loop from back to front to maintain the stability.
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


print(counting_sort_stable([4, 2, 2, 8, 3, 3, 1]))
