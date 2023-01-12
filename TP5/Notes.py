x = 0

valeur1 = str(input("Veuillez entrer la note du moudule 1 et le coefficient correpondant:"))
valeur2 = str(input("Veuillez entrer la note du moudule 2 et le coefficient correpondant:"))
valeur3 = str(input("Veuillez entrer la note du moudule 3 et le coefficient correpondant:"))
valeur4 = str(input("Veuillez entrer la note du moudule 4 et le coefficient correpondant:"))
valeur5 = str(input("Veuillez entrer la note du moudule 5 et le coefficient correpondant:"))

s2 = valeur1.split(" ")
s3 = int(s2[0])
s4 = int(s2[1])

s5 = valeur2.split(" ")
s6 = int(s5[0])
s7 = int(s5[1])

s8 = valeur3.split(" ")
s9 = int(s8[0])
s10 = int(s8[1])

s11 = valeur4.split(" ")
s12 = int(s11[0])
s13 = int(s11[1])

s14 = valeur5.split(" ")
s15 = int(s14[0])
s16 = int(s14[1])

print("La note du module 1 de l'étudiant est de:",s3,"et le coeffciant du module est de:",s4)

print("La note du module 1 de l'étudiant est de:",s6,"et le coeffciant du module est de:",s7)

print("La note du module 1 de l'étudiant est de:",s9,"et le coeffciant du module est de:",s10)

print("La note du module 1 de l'étudiant est de:",s12,"et le coeffciant du module est de:",s13)

print("La note du module 1 de l'étudiant est de:",s15,"et le coeffciant du module est de:",s16)

x = ((s3*s4) + (s6*s7) + (s9*s10) + (s12*s13) + (s15*s16))/(s4 + s7 + s10 + s13 + s16)
print("la moyenne est de l'étudiant est de:", x)

if x >= 10 and s3 > 8 and s6 > 8 and s9 > 8 and s12 > 8 and s15 > 8:
    print("l'étudiant est admis")
else:
    print("l'étudiant n'est pas admis")





