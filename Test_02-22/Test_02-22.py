k, m, n = int(input()), int(input()), int(input())
if n <= k:
    print(2 * m)
elif n % k == 0:
    print(2 * m * n // k)
else:
    print(2 * m * (1 + n // k))
