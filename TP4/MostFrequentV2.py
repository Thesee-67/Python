L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7, 6]
y = 0
nombre = L1[0]
for i in L1:
    x = L1.count(i)
    if x > y:
        y = x
        nombre = i
print("Le nombre le plus frequent",nombre,"(",x,"x).")

