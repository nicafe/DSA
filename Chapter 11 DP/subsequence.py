def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Fill in DP table.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Get the longest common subsequence through backtracking.
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs


def longest_common_subsequence_optimized(str1, str2):
    m, n = len(str1), len(str2)
    dp = [0] * (n + 1)  # Use 1 dimentional array instead of 2 dimentional table.
    # # Use DP array in turn.
    for i in range(1, m + 1):
        prev = 0  # prev stores value of upper left corner, set it to 0 for the first column.
        for j in range(1, n + 1):
            temp = dp[j]  # Save the current value for the next prev.
            if str1[i - 1] == str2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp  # Update prev.

    return dp[n]

str1 = "abcde"
str2 = "ace"
print(longest_common_subsequence(str1, str2))

