from tkinter import *
from tkinter.colorchooser import *
from random import *

# valeur par défaut
size = 'petit'
x1 = 100
x2 = 200
y1 = 100
y2 = 200
color = '#fff'
dash = ''
ori = 'verticale'
ecartement = 'petit'
space = 10


def taille():
    def petit():
        global size, x1, x2, y1, y2
        size = 'petit'
        x1 = randint(0, 200)
        y1 = randint(0, 200)
        x2 = randint(x1, x1 + 200)
        y2 = y1 - (x2 - x1)
        popup.destroy()

    def moyen():
        global size, x1, x2, y1, y2
        size = 'moyen'
        x1 = randint(200, 400)
        y1 = randint(200, 400)
        x2 = randint(x1 + 200, x1 + 400)
        y2 = y1 - (x2 - x1)
        popup.destroy()

    def grand():
        global size, x1, x2, y1, y2
        size = 'grand'
        x1 = randint(400, 600)
        y1 = randint(400, 600)
        x2 = randint(x1 + 400, x1 + 600)
        y2 = y1 - (x2 - x1)
        popup.destroy()

    popup = Tk()
    popup.geometry('200x100')
    Label(popup, text="De quelle taille doit être le carré ?").pack()
    Button(popup, text="Petit (<200px)", width=20, command=petit).pack()
    Button(popup, text="Moyen (200px<<400px)", width=20, command=moyen).pack()
    Button(popup, text="Grand (>400px)", width=20, command=grand).pack()


def couleur():
    global color
    color = askcolor()
    color = color[1]


def hatchType():
    def pleine():
        global dash
        dash = ''
        popup.destroy()

    def hachee():
        global dash
        dash = 1, 2
        popup.destroy()

    popup = Tk()
    popup.geometry('200x100')
    Label(popup, text="Choisissez le type d'hachure").pack()
    Button(popup, text="Pleine", width=20, command=pleine).pack()
    Button(popup, text="Hachée", width=20, command=hachee).pack()


def hatchOrientation():
    def verticale():
        global ori
        ori = 'verticale'
        popup.destroy()

    def horizontale():
        global ori
        ori = 'horizontale'
        popup.destroy()

    def cadrille():
        global ori
        ori = 'cadrille'
        popup.destroy()

    popup = Tk()
    popup.geometry('200x100')
    Label(popup, text="Choisissez l'orientation des hachures").pack()
    Button(popup, text="Verticale", width=20, command=verticale).pack()
    Button(popup, text="Horizontale", width=20, command=horizontale).pack()
    Button(popup, text="Cadrillée", width=20, command=cadrille).pack()


def hatchSpread():
    def petit():
        global ecartement, space
        ecartement = 'petit'
        space = randint(5, 10)
        popup.destroy()

    def moyen():
        global ecartement, space
        ecartement = 'moyen'
        space = randint(10, 20)
        popup.destroy()

    def grand():
        global ecartement, space
        ecartement = 'grand'
        space = randint(20, 30)
        popup.destroy()

    popup = Tk()
    popup.geometry('200x100')
    Label(popup, text="Choisissez l'espace entre les hachures").pack()
    Button(popup, text="Petit (<10px)", width=20, command=petit).pack()
    Button(popup, text="Moyen (10px<<20px)", width=20, command=moyen).pack()
    Button(popup, text="Grand (>20px)", width=20, command=grand).pack()


def generate():
    global x1, x2, y1, y2

    # centrage du dessin
    if x2 > 600:
        diff = x2 - 600
        x1 = x1 - diff
        x2 = x2 - diff

    if y2 < 0:
        diff = 0 - y2
        y1 = y1 + diff
        y2 = y2 + diff

    dessin.create_rectangle(x1, y1, x2, y2, fill=color)

    # génération du type de hachure
    # type verticale
    if ori == 'verticale':
        i = x1
        while i < x2:
            dessin.create_line(i, y1, i, y2, dash=(dash))
            i = i + space

    # type horizontale
    if ori == 'horizontale':

        if y1 > y2:
            i = y1
            while i > y2:
                dessin.create_line(x1, i, x2, i, dash=(dash))
                i = i - space

        if y1 < y2:
            i = y1
            while i < y2:
                dessin.create_line(x1, i, x2, i, dash=(dash))
                i = i + space

    # type cadrillée
    if ori == 'cadrille':
        i = x1
        while i < x2:
            dessin.create_line(i, y1, i, y2, dash=(dash))
            i = i + space

        if y1 > y2:
            i = y1
            while i > y2:
                dessin.create_line(x1, i, x2, i, dash=(dash))
                i = i - space

        if y1 < y2:
            i = y1
            while i < y2:
                dessin.create_line(x1, i, x2, i, dash=(dash))
                i = i + space


source = Tk()
source.geometry('1100x800')

fenetre = Canvas(source, width=1100, height=800)
fenetre.pack()

# espace de dessin
dessin = Canvas(source, width=600, height=600, bg="white")
dessin.place(x=400, y=100)

# trait séparateur boutons/espace de dessin
fenetre.create_line(300, 780, 300, 20)

# boutons
taille = Button(fenetre, text="Taille", width=20, height=5, command=taille)
taille.place(x=20, y=100)

couleur = Button(fenetre, text="Couleur", width=20, height=5, command=couleur)
couleur.place(x=20, y=200)

hatchType = Button(fenetre, text="Type d'hachure", width=20, height=5, command=hatchType)
hatchType.place(x=20, y=300)

hatchOrientation = Button(fenetre, text="Orientation hachure", width=20, height=5, command=hatchOrientation)
hatchOrientation.place(x=20, y=400)

hatchSpread = Button(fenetre, text="Ecartement hachure", width=20, height=5, command=hatchSpread)
hatchSpread.place(x=20, y=500)

generate = Button(fenetre, text="GENERATION DU CARRÉ", width=30, height=5, command=generate)
generate.place(x=20, y=650)

# fenetre de test
test = Tk()
bouton1 = Button(test, text='test de la taille', command=lambda: print(size, x1, x2, y1, y2))
bouton1.pack()
bouton2 = Button(test, text='test de la couleur', command=lambda: print(color))
bouton2.pack()
bouton3 = Button(test, text='test type de hachure', command=lambda: print(dash))
bouton3.pack()
bouton4 = Button(test, text='test orientation hachure', command=lambda: print(ori, x1, x2, y1, y2))
bouton4.pack()
bouton5 = Button(test, text='test ecartement hachure', command=lambda: print(ecartement, space))
bouton5.pack()

source.mainloop()
test.mainloop()
