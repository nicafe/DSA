def permutation(lst, res=[]):
    if lst == []:
        print(res)
    else:
        for i in range(len(lst)):
            permutation(lst[:i] + lst[i + 1:], res + [lst[i]])


# permutation(list(range(4)))


def permutation_count(lst, res=[], memo={'count': 0}):
    if lst == []:
        memo['count'] += 1
        if memo['count'] == 1000000:
            exit(res)
    else:
        for i in range(len(lst)):
            permutation_count(lst[:i] + lst[i + 1:], res + [lst[i]], memo)


# permutation_count(list(range(10)))


def permutation_generator(lst, res=[]):
    if lst == []:
        yield res
    else:
        for i in range(len(lst)):
            yield from permutation_generator(lst[:i] + lst[i + 1:], res + [lst[i]])


# perm = permutation_generator(list(range(10)))
# for i in range(999999):
#     next(perm)
# print(next(perm))


class PermutationIterator:
    def __init__(self, lst):
        self.stack = [(lst, [])]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            lst, res = self.stack.pop()
            if lst == []:
                return res

            for i in range(len(lst) - 1, -1, -1):
                self.stack.append((lst[:i] + lst[i + 1:], res + [lst[i]]))

        raise StopIteration


perm = PermutationIterator(list(range(10)))
for i in range(999999):
    next(perm)
print(next(perm))
