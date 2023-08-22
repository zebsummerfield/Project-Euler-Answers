
abundant = []

def perfect(x):
    divisorList = []
    divisorTotal = 0
    divisor = round((x ** 0.5) + 1)
    divisorList.append(str(1))
    while divisor > 2:
        divisor -= 1
        if x % divisor == 0:
            divisorList.append(str(int(divisor)))
            pair = x / divisor
            if not pair == divisor:
                divisorList.append(str(int(pair)))
    for d in divisorList:
        divisorTotal += int(d)
    if x / divisorTotal < 1:
        abundant.append(str(x))


x = 1
while x < 28124:
    perfect(x)
    x += 1

sumTwoAbundant = []
numbers = range(1,28124)
notUsed = abundant
for a in abundant:
    for i in notUsed:
        sumTwo = int(a)+ int(i)
        if sumTwo < 28124:
            sumTwoAbundant.append(str(sumTwo))
        else:
            break
            

sumNumbers = sum(range(1,28124))
actualSumTwoAbundant = list(set(sumTwoAbundant))
totalSumTwoAbundant = 0
for n in actualSumTwoAbundant:
    totalSumTwoAbundant += int(n)

notSumTwoAbundant = sumNumbers - totalSumTwoAbundant

print(notSumTwoAbundant)
            
            
