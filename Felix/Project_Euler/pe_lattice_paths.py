def lattice_paths(x, y, memo={}):
    grid = (x, y)
    if grid in memo:
        return memo[grid]
    if x == 0 or y == 0:
        return 1
    memo[grid] = lattice_paths(x - 1, y) + lattice_paths(x, y-1)
    return memo[grid]

print(lattice_paths(20, 20))



