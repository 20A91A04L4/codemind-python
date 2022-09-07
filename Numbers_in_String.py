s=input()
n='1234567890'
a=list(s)
b=[]
c=0
for i in a:
    if i in n:
        b.append(i)
for i in b:
    c=c+int(i)
print(c)
    