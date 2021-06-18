x = int(input())
n = 0
while x != 0:
    y = x
    x = int(input())
    if x > y:
        n += 1
print(n)
