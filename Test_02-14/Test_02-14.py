a = int(input())
b = int(input())
c = int(input())
a2 = a % 2
b2 = b % 2
c2 = c % 2
if (a2 == 0 or b2 == 0 or c2 == 0) and (a2 == 1 or b2 == 1 or c2 == 1):
    print("YES")
else:
    print("NO")
