n=int(input())
s=n
a,b=len(str(n)),0
while n:
    d=n%10
    n=n//10
    b+=d**a
    a-=1
    
print(b==s)
    