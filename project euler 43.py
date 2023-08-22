
import itertools
perms = list(itertools.permutations(["9","8","7","6","5","4","3","2","1","0"]))
primes = [2, 3, 5, 7, 11, 13, 17]
pans_with_sub = []

for perm in perms:
    sub_property = True
    for i in range(7):
        if not int(perm[i+1] + perm[i+2] + perm[i+3]) % primes[i] == 0:
            sub_property = False
    if sub_property:
        print(perm)
        pans_with_sub.append(int("".join(perm)))

total = sum(pans_with_sub)
print(total)
        
