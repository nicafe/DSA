def print_to_iter(n):
    for i in range(n + 1):
        print(i)

def print_to(n):
    if n != 0:
        print_to(n - 1)
    print(n)

print_to_iter(5)
print_to(5)
