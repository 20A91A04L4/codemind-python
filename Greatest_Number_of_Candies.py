n = int(input())
a = list(map(int,input().split()))
b=int(input())
c=max(a)
d=[]
for i in a:
    if (i+b)>=c:
        d.append(True)
    else:
        d.append(False)
print(*d)