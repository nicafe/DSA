def steal(items, capacity):
    length = len(items)
    grid = [[0] * (capacity + 1) for x in range(length + 1)]
    
    for i in range(1, length + 1):
        weight = items[i - 1]['weight']
        value = items[i - 1]['value']
        for j in range(1, capacity + 1):
            if weight <= j:
                grid[i][j] = max(grid[i - 1][j], grid[i - 1][j - weight] + value)
            else:
                grid[i][j] = grid[i - 1][j]
    
    selected = []
    i, j = length, capacity
    while i > 0 and j > 0:
        if grid[i][j] != grid[i - 1][j]:
            selected.append(items[i - 1]['name'])
            j -= items[i - 1]['weight']
        i -= 1
    
    grid.pop(0)
    for col in grid:
        col.pop(0)
    
    return grid, selected
   
    
items = [
    {'name': 'guitar', 'weight': 1, 'value': 1500},
    {'name': 'stereo', 'weight': 4, 'value': 3000},
    {'name': 'laptop', 'weight': 3, 'value': 2000},
    ]

print(steal(items, 4))