def cal_average(num):
    sun_num = 0
    for t in num:
        sun_num = sun_num + t
    
    avg = sun_num = sun_num/ len(num)
    return avg

nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
i = 0

for i in range(nombreEtudiants) :
    i = i +1
    note_test = int(input(F"La note de l'étudiant est {i} : "))
    notes.append(note_test)

print("la moyenne est de :", cal_average(notes))
print("\n")
print ("Num de l'étudiant | note | ecart")

for i in range(nombreEtudiants) :
    print(F'{i} | {notes[i]} | {cal_average(notes) - notes[i]}')
    i = i +1