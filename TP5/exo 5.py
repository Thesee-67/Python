heuredetravail = int(input("nombre d'heure de travail:"))
salaire = int(input("salaire payer par heure:"))
a = 0
b = 0
c = 0

if heuredetravail > 200:
    heure = heuredetravail-200
    print("heure de travail majorer a 50%:",heure)
    a = (salaire*1.50)*heure
    heuredetravail = heuredetravail-heure
    print("heure de travail restant:",heuredetravail)

if 161 <= heuredetravail <= 200:
    heure1 = heuredetravail-160
    print("heure de travail majorer a 25%:",heure1)
    b = (salaire*1.25)*heure1
    heuredetravail = heuredetravail - heure1
    print("heure de travail restant:",heuredetravail)

if heuredetravail <= 160:
    heure2 = heuredetravail
    print("heure de travail avec salaire horaire",heure2)
    c = salaire*heure2
    heuredetravail = heuredetravail - heure2
    print("heure de travail:",heuredetravail)

paye = a + b + c
print("Le salaire de l'ouvrier est de:",paye,"€")
