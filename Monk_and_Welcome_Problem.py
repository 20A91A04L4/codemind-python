a=int(input())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
result = [] 
small_list = len(list1) < len(list2) and list1 or list2
for i in range(0, len(small_list)): 
	result.append(list1[i] + list2[i]) 
print(*result)