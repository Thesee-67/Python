d = int(input("Donnez l’heure de début de la location (un entier) :"))
f = int(input("Donnez l’heure de fin de la location (un entier) :"))

print (d)
print (f)


while d == f or d < 0 or d > 25 or f:
    if (d == f):
        print( "Attention ! l’heure de fin est identique à l’heure de début.")
    elif (d > f):
        print("Attention ! le début de la location est après la fin ...")
    elif (d<f):
        print("Attention ! la fin de la location est après le début ...")

heure = f - d
if d >= 0 or d < 7 
    


        


