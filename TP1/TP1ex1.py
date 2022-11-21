nom = "toto"
prenom = "titi"
math = 10
anglais = 15
info = 16
promotion = 2022
moy = (math + anglais + info)/3


print (type(nom), type(prenom), type(math), type(anglais), type(info), type(promotion))
print (" L’étudiant toto titi de la promotion", promotion, "a une moyenne de {:.2f}".format(moy))
