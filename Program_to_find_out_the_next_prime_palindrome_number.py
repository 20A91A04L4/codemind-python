def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def ispal(n):
    rev = 0
    tmp = n
    while n : 
        rev = rev * 10 + n % 10;
        n //= 10
    return rev == tmp 
n = int(input())
n += 1
while 1 :
    if isprime(n) and ispal(n):
        print(n)
        break
    n += 1