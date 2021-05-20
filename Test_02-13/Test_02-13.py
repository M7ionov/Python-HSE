a = int(input())
b = int(input())
c = int(input())
if a + b > c or b + c > a or a + c > b:
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("rectangular")
    elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
