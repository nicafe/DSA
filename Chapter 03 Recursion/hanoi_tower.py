def move(n, a, b, c):
    if n == 1:
        print(f'{a} -> {c}')
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)


move(3, 'a', 'b', 'c')
