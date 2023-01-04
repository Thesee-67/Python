dico = {
    "firstname": "Olivier",
    "name": "Guittet",
    "promo": 2022,
    "group": "RT111"
}

print(f"Votre nom est {dico['name']}, prénom est {dico['firstname']}, "
      f"vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")

# partie 2
dic = {
    "name": "toto",
    "firstname": "tata",
    "promo": 2022,
    "group": 202
}

print("Les clés sont :")
for i in dic.keys():
    print(f"-{i}")

print("Les valeurs sont :")
for i in dic.values():
    print(f"-{i}")

print("Les tuplets sont :")
for i in dic.items():
    print(f"-{i}")

binome = {
    1: dico,
    2: dic
}

print("Les étudiants formants le binôme sont :")
for i in binome.values():
    print(f"- L'étudiant {i['name']} {i['firstname']} du groupe {i['group']}")
