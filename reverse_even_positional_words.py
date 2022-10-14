a=input().split()
b=[]
for i in range(0,len(a)):
    if i%2==0:
        b.append(a[i][::-1])
    else:
        b.append(a[i])
print(*b)
        
        
        