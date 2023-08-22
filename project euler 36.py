
palin_sum = 0
for i in range(1,1000000):
    if str(i) == str(i)[::-1]:
        if bin(i).split("b")[1] == bin(i).split("b")[1][::-1]:
            print(i)
            print(bin(i))
            palin_sum += i
print(palin_sum)

