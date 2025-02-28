def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0  # str1's end index.
    # Fill in DP table.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    
    # Extract the longest common substring.
    return str1[end_index - max_length:end_index]


def longest_common_substring_optimized(str1, str2):
    m, n = len(str1), len(str2)
    dp = [0] * (n + 1)  # Use 1 dimentional array instead of 2 dimentional table.
    max_length = 0
    end_index = 0  # str1's end index.
    # Use DP array in turn.
    for i in range(1, m + 1):
        prev = 0  # prev stores value of upper left corner, set it to 0 for the first column.
        for j in range(1, n + 1):
            temp = dp[j]  # Save the current value for the next prev.
            if str1[i - 1] == str2[j - 1]:
                dp[j] = prev + 1
                if dp[j] > max_length:
                    max_length = dp[j]
                    end_index = i
            else:
                dp[j] = 0
            prev = temp  # Update prev.
    # Extract the longest common substring.
    return str1[end_index - max_length:end_index]

str1 = 'abcdef'
str2 = 'zbcdf'
print(longest_common_substring(str1, str2))
