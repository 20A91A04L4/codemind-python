a=input()
alp='abcdefghijklmnopqrstuvwxyz '
b=a.lower()
c=0
for i in b:
    if i not in alp:
        c+=1
print(c)
        