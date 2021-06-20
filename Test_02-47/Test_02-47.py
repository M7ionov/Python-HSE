a1, a2, a3 = int(input()), int(input()), int(input())
i, count, min = 3, 0, 0
while a3 !=0:
    if a2 > a1 and a2 > a3:
        count += 1
        if count == 1:
            max = i
        elif count == 2:
            s = i - max
            min = s
            max = i
        elif count > 2:
            s = i - max
            if s < min:
                min = s
            max = i
    a1 = a2
    a2 = a3
    a3 = int(input())
    i += 1
print(min)
