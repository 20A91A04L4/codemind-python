n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(len(str(i)))
c=max(b)
for i in a:
    if len(str(i))==c:
        print(i,end=" ")