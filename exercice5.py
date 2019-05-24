# Ecrire un script permettant de poser la question ‘ voulez-vous jouer ? ’.
# • Si la réponse est ‘ o ’ ou ‘ O ’ vous afficherez ‘ c ’est parti ! ’. Si la réponse est ‘ n ’ ou ‘ N ’ vous afficherez ‘ tant pis ’.

def exercice5():
    while True:
        try:
            # création des variables
            a = str(input("Voulez-vous jouer ? (O,o ; N,n)"))

            # mise en place des conditions
            if a == 'O' or a == 'o':
                print("C'est parti !")

            elif a == 'N' or a == 'n':
                print("Tant pis !")

            # rappel de la fonction en cas de mauvais input
            else:
                print("Cette action n'existe pas !\n")
                exercice5()

            # choix d'après calcul
            reload = str(input("Voulez-vous recommencer ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous recommencer ? (o/n)\n")

            if reload == "o":
                exercice5()
            else:
                break

        except:
            print("Mauvais input !")
            continue


exercice5()
