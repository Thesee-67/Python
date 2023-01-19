def ajouter_elt(lst2, elt):
    lst2.append(elt)
    return lst2

lst1 = [0, 1, 2]
lst2 = [lst1]
elt = len(lst1)
ajouter_elt(lst2, elt)
print(ajouter_elt(lst2,elt))
print("ID de la liste 2: ", id(lst2))
print(lst1)
print("ID de la liste 1: ", id(lst1))
#l'id de la liste est le meme au début mais a la fin il est différent.
 