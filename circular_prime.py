def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def reverse(n):
    rev = 0
    while n : 
        rev = rev * 10 + n % 10;
        n //= 10
    return rev
n = int(input())
if isprime(n):
    if(isprime(reverse(n))):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")