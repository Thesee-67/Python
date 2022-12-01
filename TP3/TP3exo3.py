import random 
nombre = int(input("Entrez un nombre entier entre 0 et 100:"))
compteur = 0

x = random.randrange(0,101)
while nombre > 100:
    nombre = int(input("Entrez un nombre entier entre 0 et 100:"))
while nombre < 100:
    if nombre > x:
        print("le nombre est plus petit")
        compteur= compteur+1
        nombre = int(input("Entrez un nombre entier entre 0 et 100:"))
    elif nombre < x:
        print("le nombre est plus grand")
        nombre = int(input("Entrez un nombre entier entre 0 et 100:"))
        compteur = compteur+1
    elif nombre == x:
        break
print("le nombre est égale")
print("le nombre totale d'essai est de",compteur)
