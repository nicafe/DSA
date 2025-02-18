from itertools import permutations, combinations, product


def prod_loop(iter):
    for i in range(len(iter)):
        for j in range(len(iter)):
            print((iter[i], iter[j]))


def perm_loop(iter):
    for i in range(len(iter)):
        for j in range(len(iter)):
            if i == j:
                continue
            print((iter[i], iter[j]))


def comb_loop(iter):
    for i in range(len(iter)):
        for j in range(i + 1, len(iter)):
            print((iter[i], iter[j]))


def prod(iter, r, res=[]):
    if r == 0:
        print(res)
    else:
        for i in range(len(iter)):
            prod(iter, r - 1, res + [iter[i]])


def perm(iter, r, res=[]):
    if r == 0:
        print(res)
    else:
        for i in range(len(iter)):
            perm(iter[:i] + iter[i + 1:], r - 1, res + [iter[i]])


def comb(iter, r, res=[]):
    if r == 0:
        print(res)
    else:
        for i in range(len(iter)):
            perm(iter[i + 1:], r - 1, res + [iter[i]])


def permutation_generator(iter, r, res=[]):
    if r == 0:
        yield res
    else:
        for i in range(len(iter)):
            yield from permutation_generator(iter[:i] + iter[i + 1:], r - 1, res + [iter[i]])


class PermutationIterator:
    def __init__(self, iter, r):
        self.stack = [(iter, r, [])]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            iter, r, res = self.stack.pop()
            if r == 0:
                return res

            for i in range(len(iter) - 1, -1, -1):
                self.stack.append((iter[:i] + iter[i + 1:], r - 1, res + [iter[i]]))

        raise StopIteration


# prod_loop('ABCD')
# prod('ABCD', 2)

# prod1 = product('ABCD', repeat=2)
# for i in prod1:
#     print(i)


# comb_loop('ABCD')
# comb('ABCD', 2)

# comb1 = combinations('ABCD', 2)
# for i in comb1:
#     print(i)


# perm_loop('ABCD')
# perm('ABCD', 2)

# perm1 = permutations('ABCD', 2)
# perm2 = permutation_generator('ABCD', 2)
# perm3 = PermutationIterator('ABCD', 2)
# for i in perm1:
#     print(i)
