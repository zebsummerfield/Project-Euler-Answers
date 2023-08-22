num=13195
n=1
p=2
while n<=13195:
    while p<=n-1:
        if num%n==0 and not n%p==0:
            print(n)
        p+=1
    return p
    n+=1
        
    
