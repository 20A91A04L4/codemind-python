n=int(input())
a=list(map(int,input().split()))
b=[]
for j in a :
    if j in b:
        continue
    b.append(j)
c=[]
for i in b:
    c.append(i)
    c.append(a.count(i))
print(*c)