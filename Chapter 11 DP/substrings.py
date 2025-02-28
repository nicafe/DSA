def longest_common_substring(word1, word2):
    m = len(word1)
    n = len(word2)
    grid = [[0] * (n + 1) for x in range(m + 1)]
    res = 0
    index = None
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
                if grid[i][j] > res:
                    res = grid[i][j]
                    index = i
    return word1[index - res:index], res

print(longest_common_substring('fish', 'hish'))