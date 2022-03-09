p = int(input())
x = int(input())
y = int(input())
k = int(input())
sum = int((x*100 + y)*(100 + p)/100)
while k != 1:
    sum += int(sum*p/100)
    k -=1
print(int(sum/100), int(sum%100))
