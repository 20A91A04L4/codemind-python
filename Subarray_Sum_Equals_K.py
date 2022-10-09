a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
e=0
for i in range(0,len(c)):
    for j in range(i+1,len(c)+1):
            d.append((c[i:j]))
for i in d:
    if sum(i)==b:
        e+=1
print(e)