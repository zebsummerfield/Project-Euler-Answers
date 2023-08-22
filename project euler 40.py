
def champernowne(n: int) -> str:
    decimal = ""
    i = 0
    while len(decimal) < n:
        i += 1
        decimal += str(i)
    return "0." + decimal
        
decimal = champernowne(1000000).split('.')[1]
print(int(decimal[0]) *
      int(decimal[9]) *
      int(decimal[99]) *
      int(decimal[999]) *
      int(decimal[9999]) *
      int(decimal[99999]) *
      int(decimal[999999]))


