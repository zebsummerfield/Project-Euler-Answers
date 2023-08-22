a = 1
b = 1
while a < 999:
    while b < 999:
        squareA = a ** 2
        squareB = b ** 2
        squareC = squareA + squareB
        c = squareC ** 0.5
        addition = a + b + c
        if addition == 1000:
            product = a * b * c
            print(product)
        b += 1
    b = 1
    a += 1
            
    
