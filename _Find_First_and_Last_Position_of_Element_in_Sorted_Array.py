a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c not in b:
    print('-1','-1')
else:
    print(b.index(c),a-b[::-1].index(c)-1)