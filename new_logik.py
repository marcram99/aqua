# -*-encoding:Utf-8 -*




class Cadre():
    theme = ["", "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self, liste, nom):
        self.nom = nom
        self.liste_init = [Cadre.theme[x] for x in liste]
        self.liste = self.liste_init[:]
        #self.term_affiche()



    def term_affiche(self, titre=" "):
        print(titre)
        print("+--------------+--------------+")
        print("|{:^14}|{:^14}|".format(self.liste[0], self.liste[1]))
        print("|--------------+--------------|")
        print("|{:^29}|".format(self.liste[2]))
        print("|--------------+--------------|")
        print("|{:^14}|{:^14}|".format(self.liste[3], self.liste[4]))
        print("+--------------+--------------+")

    def avec_cache(self,cache):
        self.liste =[self.liste[x] if not cache.liste[x] else ('*****') for x in range(5)]
        #self.term_affiche()


class Cache():
    def __init__(self, liste, nom):
        self.liste = liste
        self.nom = nom
        #self.term_affiche()

    def term_affiche(self):
        print("+---+")
        print('|{} {}|'.format(self.liste[0], self.liste[1]))
        print('| {} |'.format(self.liste[2]))
        print('|{} {}|'.format(self.liste[3], self.liste[4]))
        print("+---+")

    def rot_h(self):
        self.liste = [self.liste[3], self.liste[0], self.liste[2], self.liste[4], self.liste[1]]
        #self.term_affiche()

    def rot_ah(self):
        self.liste = [self.liste[1], self.liste[4], self.liste[2], self.liste[0], self.liste[3]]
        #self.term_affiche()


class Plateau():
    def __init__(self):
        self.cadre1 = Cadre([1, 1, 0, 2, 3],'Cadre 1')
        self.cadre2 = Cadre([0, 3, 4, 5, 2],'Cadre 2')
        self.cadre3 = Cadre([4, 2, 5, 0, 2],'Cadre 3')
        self.cadre4 = Cadre([1, 4, 2, 0, 5],'Cadre 4')
        self.cache1 = Cache([0, 1, 1, 1, 1],'Cache 1')
        self.cache2 = Cache([0, 1, 0, 1, 1],'Cache 2')
        self.cache3 = Cache([0, 0, 1, 1, 1],'Cache 3')
        self.cache4 = Cache([0, 1, 1, 1, 0],'Cache 4')
        self.board = {'c1': self.cadre1, 'c2': self.cadre2, 'c3': self.cadre3, 'c4': self.cadre4,'x1': self.cache1, 'x2': self.cache2, 'x3': self.cache3, 'x4': self.cache4}
        self.board_state = {'c1': [], 'c2': [], 'c3': [], 'c4': [], }
        self.liste_cache_dispo = ['x1', 'x2', 'x3', 'x4']
        #self.term_affiche()

    def term_affiche(self):
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.liste[0], self.cadre1.liste[1],self.cadre2.liste[0], self.cadre2.liste[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre1.liste[2], self.cadre2.liste[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.liste[3], self.cadre1.liste[4],self.cadre2.liste[3], self.cadre2.liste[4]))
        print("+--------------+--------------+ +--------------+--------------+")
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.liste[0], self.cadre3.liste[1], self.cadre4.liste[0],
                                                       self.cadre4.liste[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre3.liste[2], self.cadre4.liste[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.liste[3], self.cadre3.liste[4], self.cadre4.liste[3],
                                                       self.cadre4.liste[4]))
        print("+--------------+--------------+ +--------------+--------------+")
        self.info_board()

    def info_board(self):
        for key,val in self.board_state.items():
            if len(val) == 0:
                info = 'pas de cache'
            else:
                info = '{} en {}'.format(self.board[val[0]].nom,val[1])
            print("{}: {}".format(self.board[key].nom, info))
        print()

    def ajoute_cache(self, cadre, cache):
        if cache in self.liste_cache_dispo:
            self.board[cadre].avec_cache(self.board[cache])
            self.board_state[cadre] = [cache,'pos0']
            self.liste_cache_dispo.remove(cache)
        else:
            print("ce cache({}) n'est pas disponible".format(cache))

    def enleve_cache(self,cadre):
        if len(self.board_state[cadre]) == 0:
            print('pas de cache sur ce cadre')
        else:
            print('{} enlevé '.format(self.board[self.board_state[cadre][0]].nom))
            self.liste_cache_dispo.remove(self.board[self.board_state[cadre][0]].nom)
            self.board_state[cadre] = []



if __name__ == '__main__':
    #cadre1 = Cadre([1, 1, 0, 2, 3])
    #cache1 = Cache([0, 1, 1, 1, 1])
    test = Cache([1,2,3,5,4],'test')
    jeu = Plateau()
    jeu.ajoute_cache('c1', 'x1')
    jeu.ajoute_cache('c2', 'x2')
    jeu.ajoute_cache('c3', 'x3')
    jeu.ajoute_cache('c4', 'x4')
    jeu.info_board()
    jeu.enleve_cache('c2')
    jeu.info_board()
    jeu.ajoute_cache('c2', 'x2')
    jeu.info_board()

