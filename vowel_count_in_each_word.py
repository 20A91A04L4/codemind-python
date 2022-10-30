words = input().split()

vowels = 'aeiouAEIOU'
for word in words:
    cnt = 0
    for char in word:
        if char in vowels:
            cnt += 1
    print(cnt, end = " ")