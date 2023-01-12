s1 = []
note = 0
coef = 0
a = 0
b = 0
c = 0
rep = 0


rep = int(input("Entrez le nombre de Module:"))
for i in range(0,rep):
    s1 = input("Veuillez entrer la note du moudule et le coefficient correpondant:")
    s2 = s1.split(" ")
    s3 = float(s2[0])
    s4 = float(s2[1])
    note =note + (s3*s4)
    coef = coef + s4
    if s3 > 8:
        a = a+0
    elif s3 == 8:
        a = a + 1
    else:
        a = a + 1 




moy = note/coef
moy = round(moy,1)



if moy >= 10:
    b = b +1
else:
    c = c+ 1



if a == 1:
    print("l'étudiant n'est pas admis")
    print("la moyenne de l'étudiant est :", moy)
elif b == 1:
    print("l'étudiant est admis")
    print("la moyenne de l'étudiant est :", moy)
elif c == 1:
    print("l'étudiant n'est pas admis")
    print("la moyenne de l'étudiant est :", moy)


