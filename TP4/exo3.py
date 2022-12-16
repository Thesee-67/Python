
nMax = 3
v1 = []
v2 = []

while True:
    n = int(input("Entrez la taille des vecteurs (entre 1 et 3) : "))
    if 1 <= n <= nMax:
        break

for i in range(n):
    v1.append(int(input("Entrez la composante de v1[{}] : ".format(i))))
    v2.append(int(input("Entrez la composante de v2[{}] : ".format(i))))


scalar_product = 0
for i in range(n):
    scalar_product += v1[i] * v2[i]

print("Le produit scalaire de V1 et V2 est : {}".format(scalar_product))