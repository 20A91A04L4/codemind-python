n=int(input())
a=input().split('0')
b=[]
for i in a:
    z=''.join(i.split())
    b.append((len(z)))
print(max(b))