n1=input()
a=int(n1)**2
n2=n1[::-1]
b=int(n2)**2
c=str(b)
d=c[::-1]
if a==int(d):
    print('True')
else:
    print('False')