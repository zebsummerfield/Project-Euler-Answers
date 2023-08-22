
largest_pandigital = 0
for i in range(1,10000):
    pandigital = ""
    n = 0
    while len(pandigital) < 9:
        n += 1
        pandigital += str(i*n)
    if len(pandigital) == 9:
        if set(pandigital) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            print((int(pandigital), i, [num for num in range(1,n+1)]))
            if int(pandigital) > largest_pandigital:
                largest_pandigital = int(pandigital)
print(largest_pandigital)
