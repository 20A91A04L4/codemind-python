import math
def isprime(n):
    if n==1 or n==0:
        return
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return
    return n
a=int(input())
b=list(map(int,input().split()))
c=min(b)
d=max(b)
e=b.index(c)
f=b.index(d)
g=0
if e<f:
    for i in range(e,f+1):
        if (isprime(b[i])):
            g+=1
else:
    for i in range(f,e+1):
        if (isprime(b[i])):
            g+=1
print(g)
