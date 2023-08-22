hex
def check_triangle(x):
    n = ((1 + 8*x)**0.5 - 1) / 2
    return n%1==0
    
def check_pentagonal(x):
    n = ((1 + 24*x)**0.5 + 1) / 6
    return n%1==0

def hexagonal(n):
    return int(n * (2*n - 1))

count = 0
while True:
    count += 1
    hexa = hexagonal(count)
    if check_triangle(hexa) and check_pentagonal(hexa):
        print(hexa)
        
