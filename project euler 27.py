
def check_prime(num):
    for i in range(2,int(abs(num)**0.5)+1):
        if num % i == 0:
            return False
    return True

    
def num_primes(a, b):
    n = 0
    while True:
        if not check_prime((n**2 + a*n + b)):
            return n
        else:
            n+=1
    return n

largest = 0
product = 0
for a in range(-999,1000):
    for b in range(-999,1000):
        consecutives = num_primes(a, b)
        if consecutives > largest:
            largest = consecutives
            product = a*b
print(largest)
print(product)
        
