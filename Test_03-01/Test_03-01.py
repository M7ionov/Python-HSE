a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
print('{:.6f}'.format(s))
