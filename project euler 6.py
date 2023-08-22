n=1
a=1
sum1=0
sum2=0

while n<=100 :
    square1=0
    square=n**2
    sum1+=square
    n+=1

while a<=100 :
    sum2+=a
    a+=1

square2=sum2**2

difference=square2-sum1

print(difference)


    
