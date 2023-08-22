
n=1
sum1=0


def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
while fib(n)<=4000000:
    if fib(n)%2==0:
         sum1+=fib(n)
    n+=1
        
print (sum1)            
            



    
