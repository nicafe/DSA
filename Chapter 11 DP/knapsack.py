def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    # Fill in DP table.
    for i in range(1, n + 1):
        weight = items[i -1]['weight']
        value = items[i - 1]['value']
        
        for j in range(1, capacity + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Get selected items through backtracking.
    selected = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected.append(items[i - 1]['name'])
            j -= items[i - 1]['weight']
        i -= 1
    selected.reverse()
    
    return dp, selected


items1 = [
    {'name': 'guitar', 'weight': 1, 'value': 1500},
    {'name': 'stereo', 'weight': 4, 'value': 3000},
    {'name': 'laptop', 'weight': 3, 'value': 2000},
    {'name': 'iphone', 'weight': 1, 'value': 2000},
    {'name': 'keyboard', 'weight': 1, 'value': 1000}
    ]

items2 = [
    {'name': 'water', 'weight': 3, 'value': 10},
    {'name': 'book', 'weight': 1, 'value': 3},
    {'name': 'food', 'weight': 2, 'value': 9},
    {'name': 'jacket', 'weight': 2, 'value': 5},
    {'name': 'camera', 'weight': 1, 'value': 6}
    ]

dp, selected = knapsack(items1, 4)
print(dp)
print(selected)
