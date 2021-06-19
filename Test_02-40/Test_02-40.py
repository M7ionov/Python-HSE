n = int(input())
f0 = 0
f1 = i = 1
while n > i:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    i += 1
print(fn)
