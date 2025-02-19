from time import sleep


def hanoi(n, a='a', b='b', c='c'):
    if n == 1:
        print(f'{a} -> {c}')
        return
    hanoi(n - 1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(n - 1, b, a, c)


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_dp(n, memo={}):
    if n <= 2:
        memo[n] = 1
    if memo.get(n) is None:
        memo[n] = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)
    return memo[n]


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def countdown(n):
    if n < 1:
        print()
        return
    print(n, end="...")
    countdown(n - 1)


hanoi(3)
