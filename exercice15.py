def lance_de():
    global tirage
    # import de la bibliotèque random
    from random import randint

    # choix d'une valeur random
    tirage = randint(0, 6)


def exercice15():
    while True:
        # choix d'après calcul
        reload = str(input("Voulez-vous lancer le dé ? (o/n)\n"))

        # filtre sur la valeur de reload
        while reload != "o" and reload != "n":
            print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
            reload = input("Voulez-vous lancer le dé ? (o/n)\n")

        if reload == "o":
            lance_de()
            print("Le dé est tombé sur", tirage)

        else:
            break


exercice15()
