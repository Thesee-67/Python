import time
import numbers


x = int(input("Rentrez un nombre entier positif:"))
somme = 0

while x < 0:
    x = int(input("Rentrez un nombre entier positif:"))
while x >= 0:
    somme = x-1
    x = x-1
    print(somme)
    if x == 0:
        break

