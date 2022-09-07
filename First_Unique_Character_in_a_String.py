a=input()
b=list(a)
c=0
for i in b:
    if b.count(i)==1:
        print(b.index(i))
        c=1
        break
if c==0:print(-1)