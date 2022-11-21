minutes = int(input("Combien de Minutes se sont écoulé depuis le début du mois"))
jour = (minutes/(60*24))+1
print("Nous somme le {:.0f}".format(jour),"jour")
