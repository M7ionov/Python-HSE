x = int(input())
y = 0
while x != 0:
    if x > y:
        y = x
        q = 1
    elif x == y:
        q += 1
    x = int(input())
print(q)
