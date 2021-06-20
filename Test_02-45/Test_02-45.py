n = int(input())
copy = n
i1, i2 = 0, 0
while n != 0:
    if n == copy:
        i2 += 1
        if i2 > i1:
            i1 = i2
    else:
        copy = n
        i2 = 1
    n = int(input())
print(i1)
