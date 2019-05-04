#création de la fonction de division afin de permettre un choix et de pouvoir l'appeler en cas d'erreur
def division():

    c = input("Souhaitez-vous une division réelle (r) ou enrière (e) ? ")

    if c == 'r':
        d = float(a) / float(b)
        print("Division réelle de ", a, "par ", b, "= ", d)

    elif c == 'e':
        d = float(a) // float(b)
        print("Division entière de ", a, "par ", b, "= ", d)

    else :
        print("Cette action n'existe pas !\n")
        division()

def exercice3():
    #début du programme, choix des deux nombres à diviser
    print("Choisir les deux nombres à diviser :\n")
    global a, b
    a = input("Nombre 1 :")
    b = input("Nombre 2 :")

    #appel de la fonction division
    division()

exercice3()