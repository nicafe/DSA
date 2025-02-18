def counting_sort(arr):
    # 1. 找到数组中的最小值和最大值
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    # 2. 初始化计数数组
    count = [0] * k

    # 3. 统计每个元素出现的次数
    for num in arr:
        count[num - min_val] += 1

    # 4. 累积计数（用于稳定排序）
    for i in range(1, k):
        count[i] += count[i - 1]

    # 5. 填充输出数组
    output = [0] * len(arr)
    for num in reversed(arr):  # 从后往前遍历以保持稳定性
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# 测试
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # 输出: [1, 2, 2, 3, 3, 4, 8]