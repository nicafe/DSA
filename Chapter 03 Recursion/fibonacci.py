def fib_loop(n):
    if n == 0:
        return 0
        
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_dp(n, memo={}):
    if n < 2:
        memo[n] = n
    if memo.get(n) is None:
        memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


print(fib_loop(35))
print(fib(35))
print(fib_dp(35))
