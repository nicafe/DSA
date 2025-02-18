def route_count_math(m, n):
    res = 1
    for i in range(m):
        res *= (m + n - i) / (m - i)

    return res


def route_count(m, n):
    if (m == 1 and n == 0) or (m == 0 and n == 1):
        return 1

    res = 0

    if m > 0:
        res += route_count(m - 1, n)
    if n > 0:
        res += route_count(m, n - 1)

    return res


def route_count_dp(m, n, memo={}):
    if (m == 1 and n == 0) or (m == 0 and n == 1):
        return 1

    if memo.get((m, n)) is None:
        res = 0

        if m > 0:
            res += route_count_dp(m - 1, n, memo)
        if n > 0:
            res += route_count_dp(m, n - 1, memo)

        memo[(m, n)] = res

    return memo[(m, n)]


print(route_count_dp(100, 100))
