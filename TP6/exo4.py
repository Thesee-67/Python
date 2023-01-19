import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for x in table if x < vseuil)

nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Quel est l'intervalle minimum ? "))
vmax = int(input("Quel est l'intervalle maximum ? "))

tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)

seuil = input("Voulez-vous préciser le seuil ? (O/N)")
if seuil.upper() == "O":
    vseuil = int(input("Quel est le seuil ? "))
else:
    vseuil = 30

total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")