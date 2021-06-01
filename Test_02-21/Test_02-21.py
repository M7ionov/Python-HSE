a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0:
    print("INF")
elif (b % a) != 0 or (c * int(-b / a) + d == 0):
    print("NO")
else:
    print(-b // a)
