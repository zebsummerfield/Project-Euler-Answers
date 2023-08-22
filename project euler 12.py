n = 1
over_five_hundred = False
largest = 0
while not over_five_hundred:
    triangle = (n * (n + 1)) / 2
    a = triangle ** 0.5
    divisors = 0
    if triangle%a == 0:
        divisors += 1
        a -= 1
    a = round(a,0)
    while a > 0:
        if triangle%a == 0:
            divisors += 2
        a -= 1
    if divisors > 500:
        print(triangle)
        over_five_hundred = True
    n += 1
    
        
    
