argent = int(input("combien d'argent avez vous?:"))
base = argent
if argent !=0:
    a=int(argent/100)
    argent=argent%100
    if argent !=0:
        b=int(argent/50)
        argent=argent%50
        if argent !=0:
            c=int(argent/20)
            argent=argent%20
            if argent !=0:
                d = int(argent/10)
                argent=argent%10
                if argent !=0:
                    e = int(argent/5)
                    argent=argent%5
                    if argent !=0:
                        f = int(argent/2)
                        argent=argent%2
                        if argent !=0:
                            g = int(argent/1)
                            argent=argent%1
                            print(base,"euros, c’est donc",a," billets de 100,",b,"de 50,",c,"de 20,",d,"de 10,",e,"pièces de 2 et",f,"pièce 1.")

