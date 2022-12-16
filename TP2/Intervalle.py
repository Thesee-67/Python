print("Nombre Ã  tester :")

x = float(input())


if (-10 <= x and (x < -2 or x == -2) or  (0 < x and (x < 1 or x == 1)) or ((x == 2 or 2 < x) and x < 3)):
    print(x, "appartient Ã  I")
else :
    print(x, "n'appartient pas Ã  I")