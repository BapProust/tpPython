from tkinter import *
from tkinter.messagebox import *


def romain(a):
    global traduction

    if a == 0:
        traduction = "Le zéro strict n'existe pas en chiffre romain"
        return traduction

    if a < 0:
        traduction = "Les chiffres négatifs sont une notion abstraite lorsque l'on parle de chiffres romains"
        return traduction

    nombre = []
    nombre.append(a % 10)
    nombre.append((a % 100) - (nombre[0]))
    nombre.append((a % 1000) - (nombre[0] + nombre[1]))

    # découpage spécial pour les milliers (et dizaine de millier etc)
    nombre.append((a - (nombre[0] + nombre[1] + nombre[2])) / 1000)

    # unité
    if nombre[0] == 0:
        nombre[0] = ""
    elif nombre[0] == 1:
        nombre[0] = "I"
    elif nombre[0] == 2:
        nombre[0] = "II"
    elif nombre[0] == 3:
        nombre[0] = "III"
    elif nombre[0] == 4:
        nombre[0] = "IV"
    elif nombre[0] == 5:
        nombre[0] = "V"
    elif nombre[0] == 6:
        nombre[0] = "VI"
    elif nombre[0] == 7:
        nombre[0] = "VII"
    elif nombre[0] == 8:
        nombre[0] = "VIII"
    elif nombre[0] == 9:
        nombre[0] = "IX"

    # dizaine
    if nombre[1] == 0:
        nombre[1] = ""
    elif nombre[1] == 10:
        nombre[1] = "X"
    elif nombre[1] == 20:
        nombre[1] = "XX"
    elif nombre[1] == 30:
        nombre[1] = "XXX"
    elif nombre[1] == 40:
        nombre[1] = "XL"
    elif nombre[1] == 50:
        nombre[1] = "L"
    elif nombre[1] == 60:
        nombre[1] = "LX"
    elif nombre[1] == 70:
        nombre[1] = "LXX"
    elif nombre[1] == 80:
        nombre[1] = "LXXX"
    elif nombre[1] == 90:
        nombre[1] = "XC"

    # centaine
    if nombre[2] == 0:
        nombre[2] = ""
    elif nombre[2] == 100:
        nombre[2] = "C"
    elif nombre[2] == 200:
        nombre[2] = "CC"
    elif nombre[2] == 300:
        nombre[2] = "CCC"
    elif nombre[2] == 400:
        nombre[2] = "CD"
    elif nombre[2] == 500:
        nombre[2] = "D"
    elif nombre[2] == 600:
        nombre[2] = "DC"
    elif nombre[2] == 700:
        nombre[2] = "DCC"
    elif nombre[2] == 800:
        nombre[2] = "DCCC"
    elif nombre[2] == 900:
        nombre[2] = "CM"

    nombre[3] = int(nombre[3])
    millier = "M"
    # concaténation des opérations de traduction
    traduction = "Traduction : \n" + nombre[3] * millier + nombre[2] + nombre[1] + nombre[0]
    return traduction


fenetre = Tk()
fenetre.title("Conversion chiffre arabe / romain")

Label(fenetre, text="Ecrire un nombre, il doit être positif !").pack()


a = int()
Champ = Entry(fenetre, textvariable=a)
Champ.focus_set()
Champ.pack()

traduction = ""
rec = Label(fenetre, textvariable=traduction)
rec.pack()

Button(fenetre, text='Traduire', command=lambda: rec.config(text=romain(int(Champ.get())))).pack()


fenetre.mainloop()
