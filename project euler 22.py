
text_file = open('p022_names.txt')
names_list = sorted(text_file.read().replace('"' , ' ').split(','))
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
total = 0

for name in names_list:
    current_name = list(name)
    score = 0
    while ' ' in current_name:
        current_name.remove(' ')
    for letter in current_name:
            score += (alphabet.index(letter) + 1)
    score = score * (names_list.index(name) + 1)
    total += score

print(total)
