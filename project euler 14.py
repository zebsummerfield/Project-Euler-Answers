number = 1
sequence = 0
longest_sequence = 0
longest_number = 0
while number < 1000000:
    n = number
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            sequence += 1
        else:
            n = (3*n) + 1
            sequence += 1
    if sequence > longest_sequence:
        longest_sequence = sequence
        longest_number = number
        print(longest_number)
    number += 1
    sequence = 0
print(longest_number)
