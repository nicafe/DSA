
def get_polys(type, lower, upper):
    def calc(type, n):
        match type:
            case 3:
                return n * (n + 1) // 2
            case 4:
                return n ** 2
            case 5:
                return n * (3 * n - 1) // 2
            case 6:
                return n * (2 * n - 1)
            case 7:
                return n * (5 * n - 3) // 2
            case 8:
                return n * (3 * n - 2)

    lst = []
    i = 1
    while True:
        p = calc(type, i)
        # or use universal formula:
        # p = (type - 2) * n * (n - 1) / 2 + n
        if p >= upper:
            return lst
        if p >= lower:
            if CHECKLIST.get(p):
                CHECKLIST[p].append(type)
            else:
                CHECKLIST[p] = [type]
            lst.append(p)
        i += 1


def check(res, i=0, res_types=[]):
    p = res[i]
    types = CHECKLIST[p]
    for type in types:
        if type not in res_types:
            if i == 5:
                print(res, sum(res))
                for poly in res:
                    print(CHECKLIST[poly], end=' ')
                print()
                print(res_types + [type])
                exit()
            check(res, i + 1, res_types + [type])


def find(res=[]):
    for p in POLYS:
        if res == []:
            find([p])
        else:
            if p in res:
                continue
            if str(p)[:2] == str(res[-1])[2:]:
                if len(res) != 5:
                    find(res + [p])
                elif str(res[0])[:2] == str(p)[2:]:
                    check(res + [p])
                    return


CHECKLIST = {}

p3 = get_polys(3, 1000, 10000)
p4 = get_polys(4, 1000, 10000)
p5 = get_polys(5, 1000, 10000)
p6 = get_polys(6, 1000, 10000)
p7 = get_polys(7, 1000, 10000)
p8 = get_polys(8, 1000, 10000)
POLYS = set(p3 + p4 + p5 + p6 + p7 + p8)

for p in list(POLYS):
    if str(p)[2] == '0':
        POLYS.remove(p)

find()
