
sum_powers = []
for i in range(2, 295245+1):
    digits = list(str(i))
    digit_powers = [int(i)**5 for i in digits]
    if i == sum(digit_powers):
        sum_powers.append(i)
print(sum(sum_powers))
