a=int(input())
b=list(map(int,input().split()))
c={}
for i in b:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1
n=max(c.values())
for i,j in c.items():
    if j==n:
        print(i)
        break