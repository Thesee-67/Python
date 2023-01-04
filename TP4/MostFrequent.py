L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7]
L2 = L1
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
o = 0
x = 0
for i in L1:
    nombre = i
    x = 0
    for i in L2:
        if nombre == L2[i]:
            x += 1
        if x > o:
            o = x
            n2 = i
print("Le nombre le plus frequent dans la liste est le",n2,o,"x.")
"""
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
