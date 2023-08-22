
a = (2520)
divisible = False
remainder = False
b = 10

while not divisible :
    a += (2520)
    remainder = False
    while not remainder :
        if not a%b == 0 :
            remainder = True
            b=10
        else :
            b+=1
            if b>=20 :
                divisible = True

    print(a)

print(' ')
print(a)
print('this is the final answer')
            
        
    
