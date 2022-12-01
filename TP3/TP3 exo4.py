n = int(input("Entrez un nombre entier n:"))
y = 1
x = int(input("Entrez le nombre 1 si vous voulez utilisé la boucle for sinon si vous voulez utiliser la boucle while taper 2:"))
factoriel = 1

if x == 1:
    for i in range (1, n+1):
        factoriel = factoriel *i
        print("le factoriel est ",factoriel)
elif x == 2:
    while n >= 1:
        y *= factoriel
        factoriel += 1
        n -= 1
        print(y)
    print("le factoriel de ", n,"est",y )
