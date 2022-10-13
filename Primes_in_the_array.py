def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=list(map(int,input().split()))
e=0
for i in b:
    if is_prime(i):
        e+=1
print(e)
        