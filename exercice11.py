def exercice11():
    while True:

        try:
            # choix des valeurs
            a = float(input("Début de l'interval :\n"))
            b = float(input("Fin de l'interval :\n"))
            p = float(input("Pas :\n"))
            inf = 0
            sup = 0

            # filtre sur les valeurs de a et b
            while a >= b:
                print("Le début de l'interval doit être strictement inférieur à la fin de l'interval")
                exercice11()

            while (b - a) <= p :
                print("L'interval ne peut être inférieur à la valeur du pas")
                exercice11()

            # filtre sur la valeur du pas
            while p <= 0 or p >= 1:
                print("Le pas doit se trouver entre 0 et 1 !")
                p = float(input("Pas :\n"))

            # calcul du nombre de subdivision
            n = (b - a) / p

            # calcul de l'aire inférieure
            for i in range(0, int(n)):
                l = (b - a) / n
                h = (a + (i * (b - a) / n)) ** 2
                a2 = l * h
                inf += a2

            # calcul de l'aire supérieure
            for i in range(0, int(n)):
                l = (b - a) / n
                h = (a + ((i + 1) * (b - a) / n)) ** 2
                a2 = l * h
                sup += a2

            # moyenne des aires
            moy = (inf + sup) / 2

            print("D'après la méthode des rectangles, l'intégralle de x² sur[", a, ";", b, "] avec un pas de", p,
                  "est :", moy)

            # choix d'après calcul
            reload = str(input("Voulez-vous calculer un autre interval ? (o/n)\n"))

            # filtre sur la valeur de reload
            while reload != "o" and reload != "n":
                print("Merci de ne répondre que 'o' pour oui et 'n' pour non ")
                reload = input("Voulez-vous calculer un autre interval ? (o/n)\n")

            if reload == "o":
                exercice11()
            else :
                break

        # filtre sur la nature des inputs
        except:
            print("Mauvais input !")
            continue


exercice11()
