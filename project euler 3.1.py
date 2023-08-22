num=600851475143
n=1
p=2
while n<=600851475143:
    if num%n==0:
        p=2
        if p<=n-1:
            if not n%p==0:
                print(n)
            p+=1
    n+=1
