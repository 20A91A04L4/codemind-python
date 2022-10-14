a=input()
c=list(a)
b=input()
for i in c:
    if b not in c:
        print('False')
        break
    else:
        print('True')
        print(c.index(b))
        break