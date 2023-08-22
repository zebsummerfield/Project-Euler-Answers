def factorial(x: int) -> int:
    if x == 0:
        return 1
    else:
        total = x
        while x >= 2:
            x -= 1
            total *= x
        return total

num = 10
sum_num = 0
while num < 3000000:
    if sum([factorial(int(i)) for i in list(str(num))]) == num:
        print(num)
        sum_num += num
    num += 1
print(sum_num)
