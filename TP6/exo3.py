#a
# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt())
#il affiche la liste lst c'est a dire 0,1,2 et le nombre de valeur dans cette liste.

print(ajouter_elt())
#on remarque que le 3 apparait 2 fois a la fin de la liste contrairement a avant ou il apparait qu'une seule fois.

def ajouter_carac(ch = "abc", elt = "d"):
    return ch + elt

print(ajouter_carac())

#le résultat de la fonction ajouter carac est abcd

print(ajouter_carac())

# le résultat de la fonction est toujours le meme.