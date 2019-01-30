# -*-encoding:Utf-8 -*

import numpy as np


class Cadre():
    theme = ["", "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self, liste):
        out = [Cadre.theme[x] for x in liste]
        self.liste = np.array([[out[0],out[1]],out[2], [out[3], out[4]]])
        #self.term_affiche()


    def term_affiche(self, titre=" "):
        print(titre)
        print("+--------------+--------------+")
        print("|{:^14}|{:^14}|".format(self.liste[0][0], self.liste[0][1]))
        print("|--------------+--------------|")
        print("|{:^29}|".format(self.liste[1]))
        print("|--------------+--------------|")
        print("|{:^14}|{:^14}|".format(self.liste[2][0], self.liste[2][1]))
        print("+--------------+--------------+")

    def avec_cache(self,cache):
        bool_mask = (cache == 1)
        print(cache)
        print(bool_mask)



class Cache():
    def __init__(self, liste):
        self.liste = np.array([[liste[0],liste[1]],liste[2], [liste[3], liste[4]]])
        #self.term_affiche()

    def term_affiche(self):
        print("+---+")
        print('|{} {}|'.format(self.liste[0][0], self.liste[0][1]))
        print('| {} |'.format(self.liste[1]))
        print('|{} {}|'.format(self.liste[2][0], self.liste[2][1]))
        print("+---+")

    def rot_h(self):
        self.liste = np.array([[self.liste[2][0],self.liste[0][0]],self.liste[1], [self.liste[2][1], self.liste[0][1]]])
        #self.term_affiche()

    def rot_ah(self):
        self.liste = np.array([[self.liste[0][1],self.liste[2][1]],self.liste[1], [self.liste[0][0], self.liste[2][0]]])
        #self.term_affiche()

    def avec_cache(self):
        bool_mask = (self.liste == 1)

        print(bool_mask)
        print(self.liste)




if __name__ == '__main__':
    cadre1 = Cadre([1, 1, 0, 2, 3])
    cadre2 = Cadre([0, 3, 4, 5, 2])
    cadre3 = Cadre([4, 2, 5, 0, 2])
    cadre4 = Cadre([1, 4, 2, 0, 5])
    cache1 = Cache([0, 1, 1, 1, 1])
    cache2 = Cache([0, 1, 1, 1, 1])
    cache3 = Cache([0, 0, 1, 1, 1])
    cache4 = Cache([0, 1, 1, 1, 0])
    test = Cache([1,2,3,5,4])
    test.term_affiche()
    test.rot_h()
    test.rot_h()
    test.rot_ah()
    test.rot_ah()
    cache1.avec_cache()


