a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
maxNout = 0
maxTemp = (a1 // a2) * (b1 // b2) * (c1 // c2)
if maxTemp > maxNout:
    maxNout = maxTemp
maxTemp = (a1 // a2) * (b1 // c2) * (c1 // b2)
if maxTemp > maxNout:
    maxNout = maxTemp
maxTemp = (a1 // b2) * (b1 // a2) * (c1 // c2)
if maxTemp > maxNout:
    maxNout = maxTemp
maxTemp = (a1 // b2) * (b1 // c2) * (c1 // a2)
if maxTemp > maxNout:
    maxNout = maxTemp
maxTemp = (a1 // c2) * (b1 // a2) * (c1 // b2)
if maxTemp > maxNout:
    maxNout = maxTemp
maxTemp = (a1 // c2) * (b1 // b2) * (c1 // a2)
if maxTemp > maxNout:
    maxNout = maxTemp
print(maxNout)
