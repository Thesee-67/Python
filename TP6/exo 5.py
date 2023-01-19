import re
import unicodedata

def nettoyer_texte(texte):
    texte = re.sub(r'[^\w\s]', '', texte)
    texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode("utf-8")
    texte = texte.lower()
    return texte

def palindrome(texte):
    texte = nettoyer_texte(texte)
    return texte == texte[::-1]


texte = input("Entrez un mot/phrase : ")

if palindrome(texte):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")