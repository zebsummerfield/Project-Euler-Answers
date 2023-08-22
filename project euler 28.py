
total = 0
for i in range(1,1002):
    if i % 2 == 0:
        total += (i**2 + 1)
        total += (i**2 + 1) - i
        total += (i**2 + 1) + i
    else:
        total += (i**2)
print(total)
