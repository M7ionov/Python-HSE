x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0):
    if abs(x2 - x1) <= y2 - y1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
