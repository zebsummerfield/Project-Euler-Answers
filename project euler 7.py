prime=1
n=1

while prime<10000 :
    prime+=1
    n+=2
    squareroot=n**0.5
    a=round(squareroot,0)
    while a>1 :
        if n%a==0 :
            prime-=1
            a=1
        a-=1
    print(prime)

print(' ')
print('the 10001st prime number is...')
print(n)

            
            
