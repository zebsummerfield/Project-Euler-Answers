
def d(n):
    count = 0
    x = round( n / 2 , 0)
    while x > 0:
        if n % x == 0:
            count += x
        x -= 1
    return count

total = 0
a = 10000
while a > 0:
    b = d(a)
    if d(b) == a and not b == a:
        total += a
        total += b
    a -= 1

total = total / 2
print(total)
        
