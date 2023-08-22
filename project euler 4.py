a = 999
b = 999
largest = 0
while a > 99:
    while b > 99:
        product = a*b
        product = str(product)
        reverse = product[::-1]
        reverse = int(reverse)
        product = int(product)
        if reverse == product:
            palendrome = product
            if palendrome > largest:
                largest = palendrome
                print(largest)
        b -=1
    b = 999
    a -= 1
        
        
