x = 0

valeur1 = str(input("Veuillez entrer la note du moudule 1 et le coefficient correpondant:"))
valeur2 = str(input("Veuillez entrer la note du moudule 2 et le coefficient correpondant:"))
valeur3 = str(input("Veuillez entrer la note du moudule 3 et le coefficient correpondant:"))
valeur4 = str(input("Veuillez entrer la note du moudule 4 et le coefficient correpondant:"))
valeur5 = str(input("Veuillez entrer la note du moudule 5 et le coefficient correpondant:"))

s2 = valeur1.split(" ")
s3 = s2[0]
s4 = s2[1]

s5 = valeur2.split(" ")
s6 = s5[0]
s7 = s5[1]

s8 = valeur3.split(" ")
s9 = s8[0]
s10 = s8[1]

s11 = valeur4.split(" ")
s12 = s11[0]
s13 = s11[1]

s14 = valeur5.split(" ")
s15 = s14[0]
s16 = s14[1]

print(valeur1)
print(s3)
print(s4)

print(valeur2)
print(s6)
print(s7)

print(valeur3)
print(s9)
print(s10)

print(valeur4)
print(s12)
print(s13)

print(valeur5)
print(s15)
print(s16)

v5 = (s15*s16)
v4 = (s12*s13)
v3 = (s9*s10)
v2 = (s6*s7)
v1 = (s3*s4)

x = (v1 + v2 + v3 + v4 + v5)/5
print(x)


