#Ecrire une fonction fibonnaci récursive qui calcul la suite de Fibonnaci

def exercice17():
    while True:

        try:
            # création des inputs et variables
            tab = [1, 0, 0]
            x = 0
            y = int(input("Choisissez le n-ieme terme de la suite que vous voulez voir :\n"))

            print("Voici la suite de Fibonnaci jusqu'au numero du terme choisis :\n")

            # boucle calculant les termes de la suite de Fibonnaci (méthode assembleur)
            while x < y:
                tab[2] = tab[0] + tab[1]
                tab[0] = tab[1]
                tab[1] = tab[2]

                print(tab[1])

                x = x + 1

            print("Le", y, "eme terme de la suite de Fibonnaci est :", tab[1])

            # choix d'après calcul
            reload = str(input("Voulez-vous calculer la suite de Fibonnaci jusqu'à un autre terme ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous calculer la suite de Fibonnaci jusqu'à un autre terme ? (o/n)\n")

            if reload == "o":
                exercice17()
            else:
                break

        # filtre sur la nature des inputs
        except:
            print("Mauvais input !")
            continue


exercice17()
