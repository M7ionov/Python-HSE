x: int
x, y = int(input()), int(input())
day = 1
while x < y:
    x *= 1.1
    day += 1
print(day)
