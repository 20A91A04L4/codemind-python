n = int(input())
li = list(map(int,input().split()))
e = 0
o = 0
for i in range (0,len(li)):
    if i % 2 == 1:
        o += li[i]
    else :
        e += li[i]
if e - o == 0:
    print("YES")
else:
    print("NO")