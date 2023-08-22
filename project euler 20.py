def factorial(n):
    number = n
    while n >= 2:
        n -= 1
        number = number * n
    return number

x = list(str(factorial(100)))
total = 0

for i in x:
    total += int(i)

print(total)
    



        
