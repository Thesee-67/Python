nombre = int(input("Entrez un nombre entier:"))

if nombre == 0:
    print("le nombre vaut 0 et il est pair.")
elif nombre > 1:
    if nombre % 2 == 0:
        print("le nombre est Positif et paire.")
    else:
        print("le nombre est Positif et impaire.")
else :
    if nombre % 2 ==0:
        print("le nombre est négatif et paire")
    else:
        print("le nombre est Positif et impaire.")




