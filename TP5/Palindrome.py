corriger = ""
mot = str(input("Entrez un mot ou une phrase:"))
minuscule = str.lower(mot)
print(minuscule)

for a in minuscule:
    if (a.isalpha()) == True:
        corriger+=a
print(corriger)
