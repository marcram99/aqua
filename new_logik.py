# -*-encoding:Utf-8 -*

class Cadre():
    theme = ["", "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self, liste, nom):
        self.nom = nom
        self.liste_init = [Cadre.theme[x] for x in liste]
        self.liste_current = self.liste_init[:]
        #self.term_affiche()

    def term_affiche(self, titre=" "):
        print(titre)
        print("+--------------+--------------+")
        print("|{:^14}|{:^14}|".format(self.liste_current[0], self.liste_current[1]))
        print("|--------------+--------------|")
        print("|{:^29}|".format(self.liste_current[2]))
        print("|--------------+--------------|")
        print("|{:^14}|{:^14}|".format(self.liste_current[3], self.liste_current[4]))
        print("+--------------+--------------+")

    def mettre_cache(self,cache):
        self.liste_current =[self.liste_current[x] if not cache.liste_current[x] else ('*****') for x in range(5)]
        #self.term_affiche()

    def enleve_cache(self):
        self.liste_current = self.liste_init


class Cache():
    def __init__(self, liste, nom):
        self.nom = nom
        self.liste_init = liste
        self.liste_current = self.liste_init[:]
        #self.term_affiche()

    def term_affiche(self):
        print("+---+")
        print('|{} {}|'.format(self.liste_current[0], self.liste_current[1]))
        print('| {} |'.format(self.liste_current[2]))
        print('|{} {}|'.format(self.liste_current[3], self.liste_current[4]))
        print("+---+")

    def rot_h(self):
        self.liste_current = [self.liste_current[3], self.liste_current[0], self.liste_current[2], self.liste_current[4], self.liste_current[1]]
        #self.term_affiche()

    def rot_ah(self):
        self.liste_current = [self.liste_current[1], self.liste_current[4], self.liste_current[2], self.liste_current[0], self.liste_current[3]]
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
        self.animals = {x: 0 for x in Cadre.theme if x is not ''}
        self.board = {'c1': self.cadre1, 'c2': self.cadre2, 'c3': self.cadre3, 'c4': self.cadre4,'x1': self.cache1, 'x2': self.cache2, 'x3': self.cache3, 'x4': self.cache4}
        self.board_state = {'c1': [], 'c2': [], 'c3': [], 'c4': [], }
        self.liste_cache_dispo = ['x1', 'x2', 'x3', 'x4']
        self.challenge = {"salamandre":0, "grenouille":5, "poisson":0, "lezard":0, "tortue":0}

    def term_affiche(self):
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.liste_current[0], self.cadre1.liste_current[1], self.cadre2.liste_current[0], self.cadre2.liste_current[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre1.liste_current[2], self.cadre2.liste_current[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.liste_current[3], self.cadre1.liste_current[4], self.cadre2.liste_current[3], self.cadre2.liste_current[4]))
        print("+--------------+--------------+ +--------------+--------------+")
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.liste_current[0], self.cadre3.liste_current[1], self.cadre4.liste_current[0],
                                                       self.cadre4.liste_current[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre3.liste_current[2], self.cadre4.liste_current[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.liste_current[3], self.cadre3.liste_current[4], self.cadre4.liste_current[3],
                                                       self.cadre4.liste_current[4]))
        print("+--------------+--------------+ +--------------+--------------+")

    def informations(self, arg):
        if arg.lower() not in ['a', 'c', 'x', 'j','tot']:
            print("> {} n'est pas un argument valide".format(arg))
        else:
            if arg.lower() == 'a':
                self.info_animo()
            if arg.lower() == 'c':
                self.info_cadres()
            if arg.lower() == 'x':
                self.info_caches()
            if arg.lower() == 'j':
                self.term_affiche()
            if arg.lower() == 'tot':
                self.info_cadres()
                self.info_caches()
                self.info_animo()

    def info_caches(self):
        l_cache = [self.board[x].nom for x in self.liste_cache_dispo]
        l_cache.sort()
        dispo = ''
        for elem in l_cache:
            dispo += elem + ' '
        print('+'+len(l_cache)*8*'-'+'---------+')
        print('| dispo: {} |'.format(dispo))
        print('+' + len(l_cache) * 8 * '-' + '---------+')

    def info_cadres(self):
        print('+-------------------------+')
        for key, val in self.board_state.items():
            if len(val) == 0:
                info = 'Pas de cache    '
            else:
                info = '{} en {} '.format(self.board[val[0]].nom, val[1])
            print("|{}: {}|".format(self.board[key].nom, info))

        print('+-------------------------+')

    def info_animo(self):
        print('+----------------+')
        self.animals = {x: 0 for x in Cadre.theme if x is not ''}
        for elem in [x for x in self.board.values()]:
            for animo in elem.liste_current:
                if animo in self.animals:
                    self.animals[animo] += 1
        for key, val in self.animals.items():
            print('| {:<10} : {} |'.format(key, val))
        print('+----------------+')

    def ajoute_cache(self, *args):
        if args[0] not in self.board.keys():
            print(">{} n'est pas un cache/cadre valide".format(args[0]))
        if args[1] not in self.board.keys():
            print(">{} n'est pas un cache/cadre valide".format(args[1]))
        else:
            if args[0][:1]=='x':
                cache = args[0]
                cadre = args[1]
            else:
                cache = args[1]
                cadre = args[0]
            if cache in self.liste_cache_dispo:
                if len(self.board_state[cadre]) != 0:
                    print('>ADD: déjà {} sur {}'.format(self.board[self.board_state[cadre][0]].nom, self.board[cadre].nom))
                    self.enleve_cache(self.board_state[cadre][0])
                self.board[cadre].mettre_cache(self.board[cache])
                self.board_state[cadre] = [cache,'pos1']
                self.liste_cache_dispo.remove(cache)
                print('>ADD: ajouté {} au {}'.format(self.board[cache].nom, self.board[cadre].nom))


            else:
                print("ADD: Le {} n'est pas disponible".format(self.board[cache].nom))

    def enleve_cache(self, args):
        if args not in self.board.keys():
            print(">{} n'est pas un cache/cadre valide".format(args[0]))
        else:
            if args[:1]=='x':
                cache = args
                if cache in self.liste_cache_dispo:
                    print(">REM: Le {} n'est pas utilisé...".format(self.board[cache].nom))
                else:
                    liste_cadre = [x for x in self.board_state if len(self.board_state[x]) != 0]
                    cadre = [x for x in liste_cadre if self.board_state[x][0] == cache][0]
                    print('>REM: {} enlevé du {}'.format(self.board[cache].nom,self.board[cadre].nom))
                    self.board[cadre].enleve_cache()
                    self.liste_cache_dispo.append(cache)
                    self.board_state[cadre] = []
            if args[:1]=='c':
                cadre = args
                if self.board_state[cadre] == []:
                    print(">REM: il n'y a pas de cache sur le {}".format(self.board[cadre].nom))
                else:
                    cache = self.board_state[cadre][0]
                    print('>REM: {} enlevé du {}'.format(self.board[cache].nom, self.board[cadre].nom))
                    self.board[cadre].enleve_cache()
                    self.liste_cache_dispo.append(cache)
                    self.board_state[cadre] = []


    def rotation_cache(self, sens, cadre_cache):
        def maj_info(sens,cadre):
            pos_cache = ['pos1', 'pos2', 'pos3', 'pos4', ]
            liste_cadre = [x for x in self.board_state if len(self.board_state[x]) != 0]
            cadre = [x for x in liste_cadre if self.board_state[x][0] == cache][0]
            pos = self.board_state[cadre][1]
            indice = pos_cache.index(pos)
            new_indice = (indice + sens) % 4
            self.board_state[cadre][1] = pos_cache[new_indice]

        if cadre_cache not in self.board.keys():
            print(">{} n'est pas un cache/cadre valide".format(cadre_cache))
        elif cadre_cache[:1] == 'c' and self.board_state[cadre_cache] == []:
            print(">REM: il n'y a pas de cache sur le {}".format(self.board[cadre_cache].nom))
        elif cadre_cache[:1] == 'x' and cadre_cache in self.liste_cache_dispo:
            print(">REM: le {} n'est pas utilisé".format(self.board[cadre_cache].nom))
        else:
            if cadre_cache[:1] == 'x':
                cache = cadre_cache
            elif cadre_cache[:1] == 'c':
                cache = self.board_state[cadre_cache][0]
            if sens =='h':
                print('>REM: tourné le {} en sens horaire'.format(self.board[cache].nom))
                self.board[cache].rot_h()
                maj_info(1,cache)
            elif sens =='ah':
                print('>REM: tourné le {} en sens anti-horaire'.format(self.board[cache].nom))
                self.board[cache].rot_ah()
                maj_info(-1, cache)
            else:
                print(">REM: argument invalide pour sens")

if __name__ == '__main__':
    jeu = Plateau()
    jeu.ajoute_cache('x1', 'c1')
    jeu.ajoute_cache('x2', 'c2')
    jeu.ajoute_cache('x3', 'c3')
    jeu.ajoute_cache('x4', 'c4')
    jeu.enleve_cache('x1')
    jeu.enleve_cache('x4')
    jeu.term_affiche()



