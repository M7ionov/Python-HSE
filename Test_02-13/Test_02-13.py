a = int(input())
b = int(input())
c = int(input())
if a + b > c or b + c > a or a + c > b:
    if a > b and a > c:
        if a ** 2 == b ** 2 + c ** 2:
            print("rectangular")
        elif a ** 2 < b ** 2 + c ** 2:
            print("acute")
        elif a ** 2 > b ** 2 + c ** 2:
            print("obtuse")
    if b > a and b > c:
        if b ** 2 == a ** 2 + c ** 2:
            print("rectangular")
        elif b ** 2 < a ** 2 + c ** 2:
            print("acute")
        elif b ** 2 > a ** 2 + c ** 2:
            print("obtuse")
    if c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            print("rectangular")
        elif c ** 2 < a ** 2 + b ** 2:
            print("acute")
        elif c ** 2 > a ** 2 + b ** 2:
            print("obtuse")
    if a == b and a == c:
        print("acute")
else:
    print("impossible")
