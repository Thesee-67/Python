nom = str(input("Quelle est le nom de la première personne ?"))
prenom = str(input("Quelle est le Prénom de la première personne ?"))
nom2 = str(input("Quelle est le Nom de la deuxième personne ?"))
prenom2 = str(input("Quelle est le Prénom de la deuxième persone ?"))

if nom < nom2:
    print(str.capitalize(prenom),str.upper(nom))  
    print(str.capitalize(prenom2),str.upper(nom2))
elif nom > nom2:
    print(str.capitalize(prenom),str.upper(nom))
    print(str.capitalize(prenom2),str.upper(nom2))
elif nom == nom2:
    print(str.capitalize(prenom),str.upper(nom))
    print(str.capitalize(prenom2),str.upper(nom2))