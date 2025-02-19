def factorial_loop(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def output_loop(n):
    for i in range(n + 1):
        print(i)


def output(n):
    if n > 0:
        output(n - 1)
    print(n)


def output_pos(n, i=0):
    if n > 0:
        output_pos(n - 1, i + 1)
    print('  ' * i + str(n))


def output_rev(n, i=0):
    print('  ' * i + str(n))
    if n > 0:
        output_rev(n - 1, i + 1)


def output_pos_rev(n, i=0):
    print('  ' * i + str(n))
    if n > 0:
        output_pos_rev(n - 1, i + 1)
    print('  ' * i + str(n))


# print(factorial_loop(5))
# print(factorial(5))

# output_loop(5)
# output(5)

# output_pos(5)
# output_rev(5)
output_pos_rev(5)
