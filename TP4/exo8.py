dico = {
    "firstname": "Olivier",
    "name": "Guittet",
    "promotion": 2022,
    "groupe": "RT111"
}

print(f"Votre nom est {dico['name']}, prénom est {dico['firstname']}, " f"vous faites partie de la promotion {dico['promotion']} et votre groupe est {dico['groupe']}")

dic = {
    "name": "toto",
    "firstname": "tata",
    "promotion": 2022,
    "groupe": 202
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

print("Les étudiants formants le binôme sont: ")
for i in binome.values():
    print(f"L'étudiant {i['name']} {i['firstname']} du groupe {i['groupe']}")
