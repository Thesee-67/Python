x = int(input("Rentrez un nombre entier positif:"))
somme = 0

while x < 0:
    x = int(input("Rentrez un nombre entier positif:"))
for i in range(0, x):
    somme = x-1
    x=x-1
    print(somme)
    if x == 0:
        break