a=input()
b=['a','e','i','o','u']
c=[]
for i in a:
    if i in b:
        c.append(i)
f=set(c)
if len(f)==5:
    print('0')
for i in b:
    if i not in c:
        print(i,end=' ')
