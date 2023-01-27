n = int(input())
li = list(map(int,input().split()))
for i in range(0,n//2):
    print(li[i],li[n-i-1],end=" ")
if n%2==1 :
    print(li[n//2],0)