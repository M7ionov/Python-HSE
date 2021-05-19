n = int(input())
if (n % 10 == 1):
    print(n,"korova")
elif ((10 < n < 20) or (n % 10 == 0) or (n % 10 == 5) or (n % 10 == 6) or (n % 10 == 7) or (n % 10 == 8) or (n % 10 == 9)):
    print(n,"korov")
else:
    print(n,"korovy")
