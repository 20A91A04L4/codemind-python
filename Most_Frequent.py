def most_frequent(List):
    return max(set(List), key = List.count)
a=int(input())
b=list(map(int,input().split()))
print(most_frequent(b))

    
