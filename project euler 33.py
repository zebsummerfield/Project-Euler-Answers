
fractions = []

for i in range(10,100):
    for j in range(10, 100):
        if i < j:
            fraction = i/j
            for num in list(str(i)):
                if num in str(j) and not num == '0':
                    i_modified=int(str(i).replace(num,'',1))
                    j_modified=int(str(j).replace(num,'',1))
                    if not i_modified == 0 and not j_modified == 0:
                        fraction_modified = i_modified/j_modified
                        if fraction == fraction_modified:
                            fractions.append((i_modified, j_modified))

print(fractions)

product = [1, 1]
for frac in fractions:
    product[0] *= frac[0]
    product[1] *= frac[1]

print(product)

factors = []
for i in range(2, product[0]+1):
    if product[0]%i == 0:
        factors.append(i)

while product[0] > 1:
    for factor in factors:
        if product[1]%factor == 0:
            product[0] = product[0]/factor
            product[1] = product[1]/factor
            continue
    break

print(product)
