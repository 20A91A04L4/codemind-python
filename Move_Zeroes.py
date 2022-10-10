a=int(input())
b=list(map(int,input().split()))
d=[]
for i in b:
    if i>=1:
        d.append(i)
x=a-len(d)
for i in range(x):
    d.append(0)
print(*d)