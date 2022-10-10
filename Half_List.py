n = int(input())
a = list(map(int,input().split()))
b=[]
c=[]
for i in range(0,(len(a)//2)):
    b.append(a[i])
for i in range(len(a)//2,n):
    c.append(a[i])
d=c[::-1]
for i in b:
    d.append(i)
print(*d)