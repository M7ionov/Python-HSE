n = int(input())
f0, f1, i = 0, 1, 1
while i != n:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    i += 1
print(fn)
