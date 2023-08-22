class Day:
    month = 1
    date = 1
    day_name = 1
    year = 1900
    leap = 0

x = Day()
twentieth_century = True
count = 0

while twentieth_century:
    x.date += 1
    x.day_name += 1
    if x.day_name == 8:
        x.day_name = 1
    if x.date == 31 and ( x.month == 4 or x.month == 6 or x.month == 9 or x.month == 11 ):
        x.date = 1
        x.month += 1
    elif x.date == 32 and not( x.month == 4 or x.month == 6 or x.month == 9 or x.month == 11 or x.month == 2):
        x.date = 1
        x.month += 1
    if x.date == 29 and x.month == 2 and not x.leap == 4:
        x.date = 1
        x.month += 1
    elif x.date == 30 and x.month == 2 and x.leap == 4:
        x.date = 1
        x.month += 1
    if x.month == 13:
        x.month = 1
        x.year += 1
        x.leap += 1
    if x.leap == 5:
        x.leap = 1
        
    if x.year == 2001:
        twentieth_century = False
    if x.year > 1900 and x.date == 1 and x.day_name == 7:
        count += 1

print(count)
        

    
