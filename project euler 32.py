pandigital_products = []

for i in range(1,10000):
    for j in range(1,100):
        combined = list(str(i)+str(j)+str(i*j))
        if len(combined) == 9 and len(set(combined)) == 9 and '0' not in combined:
            pandigital_products.append(i*j)

for i in range(1,1000):
    for j in range(1,1000):
        combined = list(str(i)+str(j)+str(i*j))
        if len(combined) == 9 and len(set(combined)) == 9 and '0' not in combined:
            pandigital_products.append(i*j)
            
total = sum(set(pandigital_products))
print(total)
