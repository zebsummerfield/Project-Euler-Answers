def factorial(n):
    number = n
    while n >= 2:
        n -= 1
        number = number * n
    return number
        

def nCr(n,r):
    bi = factorial(n) / ( factorial(r) * factorial(n - r) )
    return bi

print(nCr(40,20))
