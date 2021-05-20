a = int(input())
b = int(input())
c = int(input())
a2 = a * a
b2 = b * b
c2 = c * c
if a + b > c and b + c > a and a + c > b:
    if (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2):
        print("rectangular")
    elif (a2 + b2 < c2) or (a2 + c2 < b2) or (c2 + b2 < a2):
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
