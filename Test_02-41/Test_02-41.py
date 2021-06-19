a = int(input())
f0, f1, i = 0, 1, 1
while a > f1:
    f0, f1 = f1, f0 + f1
    i += 1
if f1 != a:
    i = -1
print(0 if a == 0 else i)
