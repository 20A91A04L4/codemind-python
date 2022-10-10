n=int(input())
a=list(map(int,input().split()))
c=1
b=[]
for i in a:
    c*=i
for i in a:
    b.append(c//i)
print(*b)