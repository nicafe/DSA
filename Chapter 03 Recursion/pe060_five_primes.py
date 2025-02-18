from math import sqrt


PRIME_LIMIT = 10000
CHECKLIST_LIMIT = PRIME_LIMIT ** 2

# Prepare the checklist of primes within CHECKLIST_LIMIT.
IS_PRIME = [True for i in range(CHECKLIST_LIMIT + 1)]
IS_PRIME[0] = IS_PRIME[1] = False
for i in range(2, int(sqrt(CHECKLIST_LIMIT)) + 1):
    if IS_PRIME[i]:
        for j in range(i * i, CHECKLIST_LIMIT + 1, i):
            IS_PRIME[j] = False
print('Checklist Ready!')

# Get all primes within PRIME_LIMIT except 2 and 5.
PRIMES = [3]
for i in range(7, PRIME_LIMIT):
    if IS_PRIME[i]:
        PRIMES.append(i)
N_PRIMES = len(PRIMES)


# Recursion function.
def find(res=[], start=0):
    for i in range(start, N_PRIMES):
        prime = PRIMES[i]
        if res == []:
            find([prime], i + 1)
        else:
            flag = True
            for res_prime in res:
                num1 = int(str(res_prime) + str(prime))
                num2 = int(str(prime) + str(res_prime))
                if not IS_PRIME[num1] or not IS_PRIME[num2]:
                    flag = False
                    break
            if flag:      
                if len(res) == 4:
                    print(res + [prime], sum(res + [prime]))
                    return
                find(res + [prime], i + 1)


find()
