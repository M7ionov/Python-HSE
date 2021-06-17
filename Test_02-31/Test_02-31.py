x = int(input())
m = x
while x > 0:
    x = int(input())
    if x > m:
        m = x
print(m)
