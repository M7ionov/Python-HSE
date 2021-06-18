x = int(input())
m1 = m2 = 0
while x != 0:
    if x > m1:
        m2 = m1
        m1 = x
    elif x > m2:
        m2 = x
    x = int(input())
print(m2)
