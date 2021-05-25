k, m, n = int(input()), int(input()), int(input())
if n <= k:
    print(2 * m)
else:
    print(((2 * n + (k - 1)) // k) * m)
