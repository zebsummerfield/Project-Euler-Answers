
n = 3
prime = True
total = 5
while n < 2000000:
    squareroot = n ** 0.5
    a = round(squareroot,0)
    a = ((round((a / 2),0)) * 2) + 1
    b = 3
    while b <= a and prime:
        if n%b == 0:
            prime = False
        b += 2
    if prime:
        total += n
    n += 2
    prime = True
print(total)
    
            
    
