a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==1:
        c.append(i)
if len(c)==0:
    print('-1')
print(max(c))