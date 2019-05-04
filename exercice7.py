def exercice7():
    while True:
        print("Saisir des entiers positifs")
        print("Le compteur s'indentera tant que vous ne taperez pas d'entier négatif !")

        try:
            a = int(input())
            b = 0

            # boucle qui indente de 1 la variable b, qui sert de compteur
            while a >= 0:
                b = b + 1
                a = int(input())

            print("Le nombre d'entiers positifs rentrés est de : ", b)

            # choix d'après calcul
            reload = str(input("Voulez-vous recommencer ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous recommencer ? (o/n)\n")

            if reload == "o":
                exercice7()
            else:
                break

        except:
            print("Mauvais input !")
            continue


exercice7()
