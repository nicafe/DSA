def longest_common_subsequence(word1, word2):
    m = len(word1)
    n = len(word2)
    grid = [[0] * (n + 1) for x in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    res = ''
    i, j = m, n
    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            res = word1[i - 1] + res
            i -= 1
            j -= 1
        elif grid[i - 1][j] > grid[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return res, grid[m][n]


print(longest_common_subsequence('Racecar!', 'Race you on Mars!'))
