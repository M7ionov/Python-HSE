a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if (a <= d and b <= e) or (a <= e and b <= d):
    print("YES")
elif (c <= d and b <= e) or (c <= e and b <= d):
    print("YES")
elif (c <= d and a <= e) or (c <= e and a <= d):
    print("YES")
else:
    print("NO")
