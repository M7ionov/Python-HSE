n1, n2, up1, up2, down1, down2 = int(input()), 0, 1, 1, 1, 1
while n1 != 0:
    n1, n2 = int(input()), n1
    if n1 == 0:
        break
    elif n1 > n2:
        up2 += 1
        down2 = 1
    elif n1 < n2:
        down2 += 1
        up2 = 1
    else:
        up2, down2 = 1, 1
    if up2 >= up1:
        up1 = up2
    if down2 >= down1:
        down1 = down2
print(max(up1, down1))
