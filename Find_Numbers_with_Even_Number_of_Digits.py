a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
e=0
for i in b:
    c.append(str(i))
for i in c:
    d.append(len(i))
for i in d:
    if i%2==0:
        e+=1
print(e)