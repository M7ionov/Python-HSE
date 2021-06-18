x = int(input())
m = x
while x != 0:
    x = int(input())
    if x > m and x != 0:
        m = x
print(m)
