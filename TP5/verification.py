import os
import datetime


fichier1 = 'TP5\\f1.txt'
fichier2 = 'TP5\\f2.txt'


if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    taille1 = os.path.getsize(fichier1)
    taille2 = os.path.getsize(fichier2)
    print("La taille de", fichier1, "est de", taille1, "octets.")
    print("La taille de", fichier2, "est de", taille2, "octets.")
    temps1 = os.path.getmtime(fichier1)
    temps2 = os.path.getmtime(fichier2)
    date1 = datetime.datetime.fromtimestamp(temps1)
    date2 = datetime.datetime.fromtimestamp(temps2)
    if date1 > date2:
        print(fichier1, "est le plus récent avec une date de modification de", date1)
    elif date2 > date1:
        print(fichier2, "est le plus récent avec une date de modification de", date2)
    else:
        print("Les deux fichiers ont été modifiés à la même date :", date1)
else:
    print("Au moins un des fichiers spécifiés n'existe pas.")