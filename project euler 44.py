
def pentagonal(n):
    return int((n/2) * (3*n - 1))

def check_pentagonal(x):
    n = ((1 + 24*x)**0.5 + 1) / 6
    return n%1==0

pentagonals = [1]
pairs = []
count = 1

while True:
    count += 1
    if count%1000==0:
        print(count)
    for i in range((count-1) * 2, count * 2):
        pentagonals.append(pentagonal(i))
    for i in range(1,count):
        s = pentagonals[count-1] + pentagonals[i-1]
        d = pentagonals[count-1] - pentagonals[i-1]
        if check_pentagonal(s) and check_pentagonal(d):
            pairs.append((pentagonals[i-1], pentagonals[count-1], s, d))
            print(pairs)

