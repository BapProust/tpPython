def exercice19():
    while True:
        try:
            a = str(input("Voulez-vous créer toto.bin ou toto.txt ?(bin/txt)\n"))

            # partie toto.bin
            if a == "bin":

                # création du fichier
                with open("toto.bin", "w") as toto:

                    print(
                        "Le fichier toto.bin a été créé.\n Rentrez les deux entiers que vous voulez mettre dans le fichier :\n")

                    # input des nombres entiers
                    b = int(input())
                    c = int(input())

                    # conversion des entiers en string pour valider la syntaxe file.write(str)
                    b = str(b)
                    c = str(c)

                    # écriture des variables dans le fichier toto.bin
                    toto.write(b + ", ")
                    toto.write(c)

                print("Lecture du fichier toto.bin")

                # ouverture de toto.bin en mode lecture
                with open("toto.bin", "r") as toto:
                    print(toto.read())

            # partie toto.txt
            elif a == "txt":

                # création du fichier
                with open("toto.txt", "w") as toto:
                    print(
                        "Le fichier toto.txt a été créé.\n Rentrez les deux entiers que vous voulez mettre dans le fichier :\n")

                    # input des nombres entiers
                    b = int(input())
                    c = int(input())

                    # conversion des entiers en string pour valider la syntaxe file.write(str)
                    b = str(b)
                    c = str(c)

                    # écriture des variables dans le fichier toto.txt
                    toto.write(b + ", ")
                    toto.write(c)

                print("Lecture du fichier toto.txt")

                # ouverture de toto.txt en mode lecture
                with open("toto.txt", "r") as toto:
                    print(toto.read())

            # filtre sur l'extension de fichier
            else:
                print("Mauvais input !")
                exercice19()

            # choix d'après calcul
            reload = str(input("Voulez-vous recréer un fichier ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous recréer un fichier ? (o/n)\n")
            if reload == "o":
                exercice19()
            else:
                break

        # filtre sur la nature des inputs
        except:
            print("Mauvais input !")
            continue


exercice19()
