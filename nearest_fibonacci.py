def nearestFibonacci(num):
    if (num == 0):
        print(0)
        return
    first = 0
    second = 1
    third = first + second
    while (third <= num):
        first = second
        second = third
        third = first + second
    if (abs(third - num)==abs(second - num)):
        print(second,third)
    elif (abs(third - num)>=abs(second - num)):
        ans =  second
    else:
        ans = third
    print(ans)
n=int(input())
nearestFibonacci(n)