n = int(input())
if (n % 10 == 1):
    print(n, "korova")
elif ((10 < n < 20) or (n % 10 == (0 or 5 or 6 or 7 or 8 or 9))):
    print(n, "korov")
else:
    print(n, "korovy")
