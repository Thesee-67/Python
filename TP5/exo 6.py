from collections import Counter
t = []
e = 0
count = 0
length = 0
done = False
exist = False

word = str(input("Rentrez une chaine de caractère de maximum 100 caractère:"))

for i in range(0,100):
    if done == True:
        break
    try:
        if word[i] == True:
            done = False
    except IndexError:
        done = True

for i in word:
    t.append(i)

print(t)

for i in word:
    length+=1

print("la taille de la chaine de caractère est de ",length,"caractère")

def Check_voyelle(word, voyelle, n):
    final = [each for each in word if each in voyelle]
    print(final)
    for i in final:
        n+=1
    n = (n/length)*100
    print("il y a {:.0f}".format(n) ,"% voyelle dans la chaine de caractère")

n = 0
voyelle = "AaEeIiOoUu"
Check_voyelle(word, voyelle,n)

for a in range(length):
    if t[a] == "w":
        if t[a+1] =="a":
            if t[a+2] =="g":
                if t[a+3] =="o":
                    if t[a+4] =="n":
                        count += 1
                        chaine = "existe"
                        if count == 1:
                            e = a+1
                        else:
                            a = a 

print("la chaine de caractère wagon",chaine)
print("le nombre d'occurence est de:",count) 
print("la pemière occurence se situe au caractère :",e,)


