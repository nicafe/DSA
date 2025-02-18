def count_combinations(n, coins):
    if len(coins) == 1:
        if n % coins[0] == 0:
            return 1
        return 0

    res = 0

    for i in range(0, n // coins[0] + 1):
        left = n - coins[0] * i
        if left == 0:
            res += 1
            break
        res += count_combinations(left, coins[1:])

    return res


def count_combinations_print(n, coins, solution={}):
    if len(coins) == 1:
        if n % coins[0] == 0:
            print(solution | {coins[0]: n // coins[0]})
            return 1
        return 0

    res = 0

    for i in range(0, n // coins[0] + 1):
        left = n - coins[0] * i
        if left == 0:
            print(solution | {coins[0]: i})
            res += 1
            break
        res += count_combinations_print(left, coins[1:], solution | ({coins[0]: i} if i != 0 else {}))

    return res


coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.sort(reverse=True)
print(f'Total solutions: {count_combinations_print(10, coins)}')
