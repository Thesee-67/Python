import os
import datetime

file1 = 'C:\\Users\\og67g\\OneDrive\\Documents\\BUT RT\\Python\\TP5\\f1.txt'
file2 = 'C:\\Users\\og67g\\OneDrive\\Documents\\BUT RT\\Python\\TP5\\f2.txt'



if os.path.isfile(file1) and os.path.isfile(file2):
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)
    print("La taille de", file1, "est de", size1, "octets.")
    print("La taille de", file2, "est de", size2, "octets.")
    mod_time1 = os.path.getmtime(file1)
    mod_time2 = os.path.getmtime(file2)
    date_time1 = datetime.datetime.fromtimestamp(mod_time1)
    date_time2 = datetime.datetime.fromtimestamp(mod_time2)
    if date_time1 > date_time2:
        print(file1, "est le plus récent avec une date de modification de", date_time1)
    elif date_time2 > date_time1:
        print(file2, "est le plus récent avec une date de modification de", date_time2)
    else:
        print("Les deux fichiers ont été modifiés à la même date :", date_time1)
else:
    print("Au moins un des fichiers spécifiés n'existe pas.")