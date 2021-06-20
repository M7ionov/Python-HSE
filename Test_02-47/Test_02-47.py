a1, a2, a3 = int(input()), int(input()), int(input())
i, count, mmin = 3, 0, 0
while a3 != 0:
    if a2 > a1 and a2 > a3:
        count += 1
        if count == 1:
            mmax = i
        elif count == 2:
            s = i - mmax
            mmin = s
            mmax = i
        elif count > 2:
            s = i - mmax
            if s < mmin:
                mmin = s
            mmax = i
    a1 = a2
    a2 = a3
    a3 = int(input())
    i += 1
print(mmin)
