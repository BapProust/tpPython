# Ecrire un script permettant de saisir 10 réels au clavier
# Les ranger dans un tableau, calculer et afficher la moyenne de ces réels

def exercice13():
    # import d'une fonction de calcul de la moyenne
    from statistics import mean

    while True:

        try:
            # création du tableau et d'une variable compteur
            tab = []
            b = 1

            # boucle
            for i in range(0, 10):
                print("Rentrez 10 nombres (", b, "sur 10 )")
                a = float(input())
                tab.append(a)

                # indentation du compteur
                b = b + 1

            print("Votre tableau :", tab)
            print("Moyenne des entrées du tableau :", mean(tab))

            # choix d'après calcul
            reload = str(input("Voulez-vous créer un autre tableau ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous créer un autre tableau ? (o/n)\n")

            if reload == "o":
                exercice13()
            else:
                break

        # filtre sur la nature des inputs
        except:
            print("Mauvais input !")
            continue


exercice13()
