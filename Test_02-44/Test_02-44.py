k = int(input())
rev = 0
copy = k
q = 0
while k != 0:
    while copy > 0:
        rev = rev * 10 + copy % 10
        copy //= 10
    if rev == k:
        q += 1
    rev = 0
    k -= 1
    copy = k
print(q)
