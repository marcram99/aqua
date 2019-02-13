# -*-encoding:Utf-8 -*

class Cadre():
    theme = ["", "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self, liste, nom):
        self.nom = nom
        self.cadre_init = [Cadre.theme[x] for x in liste]
        self.cadre_current = self.cadre_init[:]
        self.cache_on = None


    def t_affiche(self):
        print('{}'.format(self.nom))
        print("+--------------+--------------+")
        print("|{:^14}|{:^14}|".format(self.cadre_current[0], self.cadre_current[1]))
        print("|--------------+--------------|")
        print("|{:^29}|".format(self.cadre_current[2]))
        print("|--------------+--------------|")
        print("|{:^14}|{:^14}|".format(self.cadre_current[3], self.cadre_current[4]))
        print("+--------------+--------------+")
        if self.cache_on is not None:
            print("Cache {} sur ce cadre".format(self.cache_on))

    def ajoute_cache(self, cache):
        self.cache_on = cache.nom
        cache.on_cadre = self.nom
        self.cadre_current =[self.cadre_current[x] if not cache.cache_current[x] else ('*****') for x in range(5)]

    def enleve_cache(self, cache):
        if self.cache_on != cache.nom:
            raise Exception("Ce cache({}) n'est pas sur ce cadre!(devrait être: {})".format(cache.nom, self.cache_on))
        self.cache_on = None
        cache.on_cadre = None
        self.cadre_current = self.cadre_init


class Cache():
    positions = ['pos1', 'pos2', 'pos3', 'pos4']
    def __init__(self, liste, nom):
        self.nom = nom
        self.on_cadre = None
        self.pos = Cache.positions[0]
        self.cache_init = liste
        self.cache_current = self.cache_init[:]

    def t_affiche(self):
        print("+---+")
        print('|{} {}|'.format(self.cache_current[0], self.cache_current[1]))
        print('| {} |'.format(self.cache_current[2]))
        print('|{} {}|'.format(self.cache_current[3], self.cache_current[4]))
        print("+---+")
        print("Cache en {} sur le cadre {} ".format(self.pos, self.on_cadre))

    def rot_h(self):
        i = Cache.positions.index(self.pos)
        self.pos = Cache.positions[(i + 1) % 4]
        self.cache_current = [self.cache_current[3], self.cache_current[0], self.cache_current[2], self.cache_current[4], self.cache_current[1]]

    def rot_ah(self):
        i = Cache.positions.index(self.pos)
        self.pos = Cache.positions[(i - 1) % 4]
        self.cache_current = [self.cache_current[3], self.cache_current[0], self.cache_current[2], self.cache_current[4], self.cache_current[1]]

class Plateau():
    def __init__(self):
        self.cadre1 = Cadre([1, 1, 0, 2, 3],'c1')
        self.cadre2 = Cadre([0, 3, 4, 5, 2],'c2')
        self.cadre3 = Cadre([4, 2, 5, 0, 2],'c3')
        self.cadre4 = Cadre([1, 4, 2, 0, 5],'c4')
        self.cache1 = Cache([0, 1, 1, 1, 1],'x1')
        self.cache2 = Cache([0, 1, 0, 1, 1],'x2')
        self.cache3 = Cache([0, 0, 1, 1, 1],'x3')
        self.cache4 = Cache([0, 1, 1, 1, 0],'x4')
        self.board = {self.cadre1.nom: self.cadre1,
                      self.cadre2.nom: self.cadre2,
                      self.cadre3.nom: self.cadre3,
                      self.cadre4.nom: self.cadre4,
                      self.cache1.nom: self.cache1,
                      self.cache2.nom: self.cache2,
                      self.cache3.nom: self.cache3,
                      self.cache4.nom: self.cache4,
                      }
    def term_affiche(self):
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.cadre_current[0], self.cadre1.cadre_current[1], self.cadre2.cadre_current[0], self.cadre2.cadre_current[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre1.cadre_current[2], self.cadre2.cadre_current[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre1.cadre_current[3], self.cadre1.cadre_current[4], self.cadre2.cadre_current[3], self.cadre2.cadre_current[4]))
        print("+--------------+--------------+ +--------------+--------------+")
        print("+--------------+--------------+ +--------------+--------------+")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.cadre_current[0], self.cadre3.cadre_current[1], self.cadre4.cadre_current[0],
                                                       self.cadre4.cadre_current[1]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^29}| |{:^29}|".format(self.cadre3.cadre_current[2], self.cadre4.cadre_current[2]))
        print("|--------------+--------------| |--------------+--------------|")
        print("|{:^14}|{:^14}| |{:^14}|{:^14}|".format(self.cadre3.cadre_current[3], self.cadre3.cadre_current[4], self.cadre4.cadre_current[3],
                                                       self.cadre4.cadre_current[4]))
        print("+--------------+--------------+ +--------------+--------------+")

    def ajoute_cache(self, *args):
        if args[0] not in self.board.keys():
            print(">ADD: '{}' n'est pas un cache/cadre valide".format(args[0]))
        if args[1] not in self.board.keys():
            print(">ADD: '{}' n'est pas un cache/cadre valide".format(args[1]))
        else:
            if args[0][0]=='x':
                cache = self.board[args[0]]
                cadre = self.board[args[1]]
            else:
                cache = self.board[args[1]]
                cadre = self.board[args[0]]
            if cache.on_cadre is not None:
                print('>ADD: cache {} pas dispo'.format(cache.nom))
            else:
                if cadre.cache_on is not None:
                    print(">ADD: il y a déjà le {} ici...".format(cadre.cache_on))
                    print('>REM: enlevé le cache {} du cadre {}'.format(cadre.cache_on, cadre.nom))
                    cadre.enleve_cache(self.board[cadre.cache_on])
                    print('>ADD: ajout de {} sur {}'.format(cache.nom, cadre.nom))
                    cadre.ajoute_cache(cache)
                else:
                    print('>ADD: ajout de {} sur {}'.format(cache.nom, cadre.nom))
                    cadre.ajoute_cache(cache)

    def enleve_cache(self, args):
        if args not in self.board.keys():
            print(">REM {} n'est pas un cache/cadre valide".format(args))
        else:
            if args[0]=='x':
                cache = self.board[args]
                if cache.on_cadre is None:
                    print(">REM: Le cache {} n'est pas utilisé...".format(cache.nom))
                else:
                    cadre = self.board[self.board[args].on_cadre]
                    print('>REM: enlevé le cache {} du cadre {}'.format(cache.nom, cadre.nom))
                    cadre.enleve_cache(cache)

            if args[0]=='c':
                cadre = self.board[args]
                if cadre.cache_on is None:
                    print(">REM: il n'y a pas de cache sur le cadre {}".format(cadre.nom))
                else:
                    cache = self.board[cadre.cache_on]
                    print('>REM: le cache {} enlevé du cadre {}'.format(cache.nom, cadre.nom))
                    cadre.enleve_cache(cache)

    def rotation_cache(self, sens, cadre_cache):
        if cadre_cache not in self.board.keys():
            print(">{} n'est pas un cache/cadre valide".format(cadre_cache))
        elif cadre_cache[:1] == 'c' and self.board[cadre_cache].cache_on is None:
            print(">REM: il n'y a pas de cache sur le {}".format(self.board[cadre_cache].nom))
        elif cadre_cache[:1] == 'x' and self.board[cadre_cache].on_cadre is None:
            print(">REM: le {} n'est pas utilisé".format(self.board[cadre_cache].nom))
        else:
            if cadre_cache[0] == 'x':
                cadre = self.board[cadre_cache]
            else:
                cadre = self.board[self.board[cadre_cache].cache_on]
            if sens =='h':
                print('>REM: tourné le {} en sens horaire'.format(self.board[cadre_cache].nom))
                cadre.rot_h()
            elif sens =='ah':
                print('>REM: tourné le {} en sens anti-horaire'.format(self.board[cadre_cache].nom))
                cadre.rot_ah()
            else:
                print(">REM: argument invalide pour sens")

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
        caches = [self.board[x] for x in self.board.keys() if self.board[x].nom[0] == 'x' ]
        dispo = ''
        long = 0
        for elem in caches:
            if elem.on_cadre is None:
                dispo += elem.nom + ' '
                long += 1
        print('+--------' + long * (3 * '-') + '+')
        print('| dispo: {}|'.format(dispo))
        print('+--------' + long * (3 * '-') + '+')

    def info_cadres(self):
        cadres = [self.board[x] for x in self.board.keys() if self.board[x].nom[0] == 'c']
        print('+-------------------------+')
        for elem in cadres:
            if elem.cache_on is not None:
                info = '{} en pos {}'.format(elem.cache_on,self.board[elem.cache_on].pos)
            else:
                info = 'pas de cache'
            print("|{}: {} |".format(elem.nom, info))

        print('+-------------------------+')
if __name__ == '__main__':
    jeu = Plateau()
    jeu.ajoute_cache('x1', 'c1')
    jeu.term_affiche()
    jeu.ajoute_cache('x2', 'c1')
    jeu.term_affiche()
    jeu.ajoute_cache('c2', 'x1')


