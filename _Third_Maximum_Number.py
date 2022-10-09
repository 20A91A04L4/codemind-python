n = int(input())
li = list(map(int,input().split()))

m1 = m2 = m3 = -1

for i in li:
    if i > m1: 
        m3 = m2
        m2 = m1
        m1 = i
    elif i < m1 and i > m2:
        m3 = m2
        m2 = i
    elif i > m3:
        m3 = i

if m3 == -1:
    print(m1)
else:
    print(m3)