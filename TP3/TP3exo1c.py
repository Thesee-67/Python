

for i in range (1, 10):
    n = int(input("Rentrez un nombre entre 0 et 20:"))
    while n < 0 or n > 20:
        n = int(input("Rentrez un nombre entre 0 et 20:"))
    if n < 10:
        print(n,"est strictement infèrieur a 10")
    elif n == 10:
        print(n,"est égale infèrieur a 10")
    else:
        print(n,"est strictement supérieur a 10")



