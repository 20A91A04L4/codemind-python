from math import sqrt
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=str(n)
b=[]
for i in a:
    if isprime(int(i)):
        b.append(i)
if len(b)==len(a) and isprime(n):
    print('Mega Prime')
else:
    print('Not Mega Prime')
        