#!/usr/bin/python3
# -*-encoding:Utf-8 -*
from tkinter import *


class Cadre(object):
    def __init__(self, cadre=[0, 0, 0, 0, 0]):
            """définit les 5 cases de notre cadre """
            self.cadre = cadre

    def matrice(self):
        return self.cadre


class Cache(object):
    model_cache = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1]]
    def __init__(self,num=0,pos=0):
        self.num = num
        self.pos = pos
        self.cache = Cache.model_cache[self.num]

    def matrice(self):
        return self.cache

    def pos_cache(self):
        return self.pos

    def rot_hor(self):
        if self.pos < 3:
            self.pos +=1
        else:
            self.pos = 0
        copie = self.cache[0:5]
        copie[0] = self.cache[3]
        copie[1] = self.cache[0]
        copie[2] = self.cache[2]
        copie[3] = self.cache[4]
        copie[4] = self.cache[1]
        self.cache = copie[0:5]


class Jeu(Tk):
    cadre1 = Cadre((1, 1, 0, 2, 3))
    cadre2 = Cadre((0, 3, 4, 5, 2))
    cadre3 = Cadre((4, 2, 5, 0, 2))
    cadre4 = Cadre((1, 4, 2, 0, 5))
    cache = []
    for nb in range (0,5):
        cache.append(Cache(nb, 0))

    def __init__(self):

        # définition de la fenêtre principale
        self.fen = Tk()
        self.fen.title("Le monde aquatique")
        self.fen.geometry("322x450+10+30")

        #self.fen_info = Tk()
        #self.fen_info.title("Moniteur d'informations")
        #self.fen_info.geometry("322x180+10+510")

        self.can = Canvas(self.fen, width=300, height =300)
        self.can.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

        self.bout_quit = Button(self.fen, text='Quitter', command=self.fen.quit).grid(row=5, column=3, columnspan=2)
        self.bout_info = Button(self.fen, text='Infos', command=self.infos).grid(row=5, column=1, columnspan=2)
        self.bout_roth = Button(self.fen, text='rot +', command=self.rotation).grid(row=5, column=2, columnspan=2)

        self.val_bouton_cadre = IntVar()
        self.bout_c1 = Radiobutton(self.fen, text='Cadre 1', variable=self.val_bouton_cadre, value=1,command=self.num_cadre).grid(row=2, column=1)
        self.bout_c2 = Radiobutton(self.fen, text='Cadre 2', variable=self.val_bouton_cadre, value=2,command=self.num_cadre).grid(row=2, column=2)
        self.bout_c3 = Radiobutton(self.fen, text='Cadre 3', variable=self.val_bouton_cadre, value=3,command=self.num_cadre).grid(row=2, column=3)
        self.bout_c4 = Radiobutton(self.fen, text='Cadre 4', variable=self.val_bouton_cadre, value=4,command=self.num_cadre).grid(row=2, column=4)

        self.val_bouton_cache = IntVar()
        self.bout_c1 = Radiobutton(self.fen, text='Cache 1', variable=self.val_bouton_cache, value=1, command=self.num_cache).grid(row=3, column=1)
        self.bout_c2 = Radiobutton(self.fen, text='Cache 2', variable=self.val_bouton_cache, value=2, command=self.num_cache).grid(row=3, column=2)
        self.bout_c3 = Radiobutton(self.fen, text='Cache 3', variable=self.val_bouton_cache, value=3, command=self.num_cache).grid(row=3, column=3)
        self.bout_c4 = Radiobutton(self.fen, text='Cache 4', variable=self.val_bouton_cache, value=4, command=self.num_cache).grid(row=3, column=4)

        self.img = []
        self.img.append(PhotoImage(file="img_vide.gif"))
        self.img.append(PhotoImage(file="img_salamandre.gif"))
        self.img.append(PhotoImage(file="img_grenouille.gif"))
        self.img.append(PhotoImage(file="img_poisson.gif"))
        self.img.append(PhotoImage(file="img_lezard.gif"))
        self.img.append(PhotoImage(file="img_tortue.gif"))

        nom,ext = "Cache",".gif"
        self.dico = {}
        for cache in range(1,5):
            for pos in range (4):
                supernom =str(nom+str(cache)+"-"+str(pos)+ext)
                self.dico[(cache,pos)] = PhotoImage(file=supernom)
        print(self.dico)


        self.img_cache = PhotoImage(file="Cache1-0.gif")

        self.fen.mainloop()

    def num_cadre(self):
        numero = self.val_bouton_cadre.get()
        if numero == 1:
            self.aff_cadre(self.cadre1.matrice())
        if numero == 2:
            self.aff_cadre(self.cadre2.matrice())
        if numero == 3:
            self.aff_cadre(self.cadre3.matrice())
        if numero == 4:
            self.aff_cadre(self.cadre4.matrice())

    def num_cache(self):
        numero = self.val_bouton_cache.get()

        self.aff_cache()

    def rotation(self):
        numero = self.val_bouton_cache.get()
        Jeu.cache[numero].rot_hor()
        self.aff_cache()

    def aff_cadre(self, cadre):
        self.cadre = cadre
        image0 = self.img[cadre[0]]
        image1 = self.img[cadre[1]]
        image2 = self.img[cadre[2]]
        image3 = self.img[cadre[3]]
        image4 = self.img[cadre[4]]
        image_vide =self.img[0]

        self.can.create_image( 50,  50, image=image0)
        self.can.create_image(250,  50, image=image1)
        self.can.create_image(150, 150, image=image2)
        self.can.create_image( 50, 250, image=image3)
        self.can.create_image(250, 250, image=image4)
        self.can.create_image( 50, 150, image=image_vide)
        self.can.create_image(150,  50, image=image_vide)
        self.can.create_image(150, 250, image=image_vide)
        self.can.create_image(250, 150, image=image_vide)

    def aff_cache(self):
        no_cache = self.val_bouton_cache.get()
        pos = Jeu.cache[no_cache].pos_cache()
        image = self.dico[(no_cache,pos)]

        self.num_cadre()
        self.can.create_image( 150,  150, image=image)



    def infos(self):
        no_cadre = self.val_bouton_cadre.get()
        no_cache = self.val_bouton_cache.get()
        cacheInfo = Jeu.cache[no_cache]

        #print("Informations du jeu : ")
        #print ("cadre: {} ".format(no_cadre))
        print("cache: {} / {} / position du cache : {} ".format(no_cache,cacheInfo.matrice(),cacheInfo.pos_cache() ))


#  ----------------Main-----------------

j = Jeu()