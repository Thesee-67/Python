L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7, 6]
o = 0
nombre = L1[0]
for i in L1:
    x = L1.count(i)
    if x > o:
        o = x
        nombre = i
print("Le nombre le plus frequent dans la liste est le",nombre,"(",x,"x).")

