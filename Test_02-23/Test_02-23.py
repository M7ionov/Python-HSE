l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
x = l1 <= r2 and l2 <= r1
y = l2 <= r3 and l3 <= r2
z = l1 <= r3 and l3 <= r1
length1 = r1 - l1
length2 = r2 - l2
length3 = r3 - l3
if x == y is True or x == z is True or y == z is True:
    print(0)
elif l2 <= r3 and l3 <= r2:
    print(1)
elif r2 <= l3 <= length1 + r2 or r3 <= l2 <= length1 + r3:
    print(1)
elif l1 <= r3 and l3 <= r1:
    print(2)
elif r1 <= l3 <= length2 + r1 or r3 <= l1 <= length2 + r3:
    print(2)
elif l2 <= r1 and l1 <= r2:
    print(3)
elif r1 <= l2 <= length3 + r1 or r2 <= l1 <= length3 + r2:
    print(3)
else:
    print(-1)
