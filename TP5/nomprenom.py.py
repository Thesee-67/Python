nom = str.upper(input("Quelle est le nom de la première personne ?"))
prenom = str.capitalize(input("Quelle est le Prénom de la première personne ?"))
nom2 = str.upper(input("Quelle est le Nom de la deuxième personne ?"))
prenom2 = str.capitalize(input("Quelle est le Prénom de la deuxième persone ?"))

if nom < nom2:
    print(prenom,nom)  
    print(prenom2,nom2)
elif nom > nom2:
    print(prenom2,nom2)
    print(prenom,nom) 
else:
    print(prenom,nom)  
    print(prenom2,nom2)
