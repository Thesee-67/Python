# a
L1 = [0]*3
print("Liste obtenue partie a : ", L1)
print("Type de la liste partie a: ", type(L1))
print("ID de la liste partie a: ", id(L1))

# b
for liste in L1:
    print("Type de l'élément partie b: ", type(liste))
    print("ID de l'élément partie b: ", id(liste))
# On remarque que id des éléments est la meme pour chaque valeur de la liste. Et que l'élément est toujours de type int

# c
L1 = [0]*3
L1[1] += 1
print("Liste obtenue partie c: ", L1)
print("Type de la liste partie c: ", type(L1))
print("ID de la liste partie c: ", id(L1))
#On remarque l'id de la liste a changer.

# d
for liste in L1:
    print("Type de l'élément partie d: ", type(liste))
    print("ID de l'élément partie d: ", id(liste))
