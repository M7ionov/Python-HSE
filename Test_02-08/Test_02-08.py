n = int(input())
m = int(input())
k = int(input())
if (k % n) != 0 and ((k % m) != 0) and (n * m) < k:
    print("NO")
else:
    print("YES")
