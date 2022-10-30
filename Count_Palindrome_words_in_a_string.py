a=input()
b=a.lower()
c=b.split()
d=0
for i in c:
    if i==i[::-1]:
        d+=1
print(d)
    