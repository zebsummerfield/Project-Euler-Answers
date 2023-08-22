import itertools

def check_prime(x: int) -> bool:
    if x == 1 or x == 0:
        return False
    checker = int(x ** 0.5 + 1)
    for i in range(2,checker):
        if x % i == 0:
            return False
    return True

prime = False
perms = list(itertools.permutations(["7","6","5","4","3","2","1"]))

for perm in perms:
    num = int("".join(perm))
    prime = check_prime(num)
    if prime:
        break

print(num)
