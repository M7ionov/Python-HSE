n = int(input())
i = 1
while i < n:
    i = i + i
if i == n:
    print('YES')
elif i > n:
    print('NO')
