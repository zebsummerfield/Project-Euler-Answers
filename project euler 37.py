def check_prime(x: int) -> bool:
    if x == 1 or x == 0:
        return False
    checker = int(x ** 0.5 + 1)
    for i in range(2,checker):
        if x % i == 0:
            return False
    return True

trunc_primes = []
x = 10
while len(trunc_primes) < 11:
    prime = True
    x += 1
    for i in range(len(str(x))):
        if not check_prime(int(str(x)[i::])) or not check_prime(int(str(x)[:i+1:])):
            prime = False
            break
    if prime:
        trunc_primes.append(x)
        print(trunc_primes)
print(sum(trunc_primes))
        
    
    
