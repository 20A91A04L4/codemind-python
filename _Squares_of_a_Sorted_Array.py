a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
d=[]
for i in c:
    d.append(i**2)
print(*sorted(d))