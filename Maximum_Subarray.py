a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(0,len(b)):
    for j in range(i+1,len(b)+1):
        c.append((b[i:j]))
for i in c:
    d.append(sum(i))
print(max(d))