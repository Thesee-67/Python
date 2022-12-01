x = int(input("Rentrez un nombre supérieur a 1:"))
nombre = 0
somme = 0

while x < 2:
        x = int(input("Rentrez un nombre supérieur a 1:"))
for i in range(0, x+1):
        somme += nombre
        if somme > x:
                break
        nombre += 1
print("le nombre recherché est ",nombre - 1)

