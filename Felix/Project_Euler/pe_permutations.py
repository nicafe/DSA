import math

def lexi_perm(arr, num):
    arr = list(arr)
    result = []
    for i in range(len(arr) - 1, -1, -1):
        fact = math.factorial(i)
        index = num // fact
        num %= fact
        result.append(str(arr.pop(index)))
    return "".join(result)

print(lexi_perm([0,1,2,3,4,5,6,7,8,9], 999999))
