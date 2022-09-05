m,n=map(int,input().split())
a=str(m)[:n]
b=str(m)[len(str(m))-n:]
print(abs(int(a)-int(b)))
