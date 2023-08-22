def check_prime(x: int) -> bool:
    checker = int(x ** 0.5 + 1)
    for i in range(2,checker):
        if x % i == 0:
            return False
    return True

count = 0
for  i in range(2,1000000):
    if check_prime(i):
        circular = True
        for j in range(len(list(str(i)))):
            if not check_prime(int(str(i)[j::] + str(i)[:j:])):
                circular = False
        if circular:
            print(i)
            count += 1
print(count)
