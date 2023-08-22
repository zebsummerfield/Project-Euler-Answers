import num2words
number_list = []
n = 1000
total = 0
while n > 0:
    a = list(num2words.num2words(n))
    while ' ' in a:
        a.remove(' ')
    while '-' in a:
        a.remove('-')
    number_list.append(str(len(a)))
    print(a)
    n -= 1
for i in number_list:
    total += int(i)
print(total)

