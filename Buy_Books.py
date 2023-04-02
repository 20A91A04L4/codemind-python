n=int(input())
a=map(int,input().split())
b=map(int,input().split())
subtracted=list()
for list1,list2 in zip(a,b):
    subtracted.append(list2-list1)
print(sum(subtracted))