for i in range(int(input())):
    s=input()
    a=s[::-1]
    if s==a:
        if len(a)%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')
    else:
        print('NO')