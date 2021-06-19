n = int(input())
f0, f1, i = 0, 1, 1
while n >= i:
    f0, f1 = f1, f0 + f1
    i += 1
print(f0)
