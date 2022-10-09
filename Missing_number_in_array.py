for i in range(int(input())):
    b=int(input())
    c=list(map(int,input().split()))
    a=[]
    for i in range(1,b+1):
        a.append(i)
    print(sum(a)-sum(c))
        