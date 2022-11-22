Base = 4
Fromage = 800.0
Eau = 2
ail = 2
pain = 400

nbConvives = int(input("Combien de convives êtes-vous?"))
print("Vous êtes",nbConvives,"Convives")

nouvelleQuantiteFromage = Fromage * nbConvives / Base
nouvelleQuantiteEau = Eau * nbConvives / Base
nouvelleQuantiteail = ail * nbConvives / Base
nouvelleQuantitepain = pain * nbConvives / Base

print("Pour",nbConvives, " convives, vous avez besoin de:")
print(nouvelleQuantiteFromage,"gr de fromage")
print(nouvelleQuantiteail,"de gousse d'ail")
print(nouvelleQuantiteEau,"dcl d'eau")
print(nouvelleQuantitepain,"gr de pain")