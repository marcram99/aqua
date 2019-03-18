# -*-encoding:Utf-8 -*
class Cadre():
    theme = ["", "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self, liste, nom):
        self.nom = nom
        self.cadre_init = [Cadre.theme[x] for x in liste]
        self.cadre_current = self.cadre_init[:]
        self.cache_on = None
        self.animal_count = Animo(self.nom, self.cadre_current)


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

    def rot_h(self, cadre):
        if self.on_cadre != cadre.nom:
            raise Exception("Ce cache({}) n'est pas sur ce cadre!(devrait être: {})".format(self.on_cadre, cadre.nom))
        i = Cache.positions.index(self.pos)
        self.pos = Cache.positions[(i + 1) % 4]
        self.cache_current = [self.cache_current[3], self.cache_current[0], self.cache_current[2], self.cache_current[4], self.cache_current[1]]
        cadre.cadre_current = cadre.cadre_init
        cadre.cadre_current = [cadre.cadre_current[x] if not self.cache_current[x] else ('*****') for x in range(5)]

    def rot_ah(self, cadre):
        if self.on_cadre != cadre.nom:
            raise Exception("Ce cache({}) n'est pas sur ce cadre!(devrait être: {})".format(self.on_cadre, cadre.nom))
        i = Cache.positions.index(self.pos)
        self.pos = Cache.positions[(i - 1) % 4]
        self.cache_current = [self.cache_current[1], self.cache_current[4], self.cache_current[2], self.cache_current[0], self.cache_current[3]]
        cadre.cadre_current = cadre.cadre_init
        cadre.cadre_current = [cadre.cadre_current[x] if not self.cache_current[x] else ('*****') for x in range(5)]


class Animo():
    def __init__(self, nom, target):
        self.nom = nom
        self.target = target
        self.animo_init = {x: 0 for x in Cadre.theme if x is not ''}
        self.animo = {x: y for x, y in self.animo_init.items()}
        
        if type(self.target) == dict:
            if 'c1' not in self.target.keys():
                for key in self.target:
                    if key in self.animo.keys():
                        self.animo[key] = self.target[key]
                self.affiche()
            else:
                ani_board = [y.cadre_current for x, y in self.target.items() if x in ['c1', 'c2', 'c3', 'c4']]
                for cadre in ani_board:
                    for elem in cadre:
                        if elem in self.animo:
                            self.animo[elem] += 1
                    self.nom = 'ani_board'
                    self.affiche()
        elif type(self.target) == list:
            for elem in target:
                if elem in self.animo:
                    self.animo[elem] +=  1
            self.affiche()

    def update(self):
        pass



    def affiche(self):
        print(self.nom)
        print('+----------------+')
        for key, val in self.animo.items():
            print('| {:<10} : {} |'.format(key, val))
        print('+----------------+')


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
        self.ani_board = Animo("ani_board", self.board)
        self.challenge01 = Animo("challenge 01", {"grenouille":5, "poisson":2})

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
            if cadre_cache[0] == 'c':
                cadre = self.board[cadre_cache]
                cache = self.board[self.board[cadre_cache].cache_on]
            else:
                cadre = self.board[self.board[cadre_cache].on_cadre]
                cache = self.board[cadre_cache]
            if sens =='h':
                print('>REM: tourné le {} en sens horaire'.format(self.board[cadre_cache].nom))
                cache.rot_h(cadre)
            elif sens =='ah':
                print('>REM: tourné le {} en sens anti-horaire'.format(self.board[cadre_cache].nom))
                cache.rot_ah(cadre)
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
        sep = 0
        print('+--------------------------+')
        for elem in caches:
            if elem.on_cadre is None:
                dispo += elem.nom + ' '
            else:
                print("| cache {} en  {} sur {} |".format(elem.nom, elem.pos, elem.on_cadre))
                sep = 1
        if sep != 0:
            print('| ------------------------ |')
        print('| disponible : {:<12}|'.format(dispo))
        print('+--------------------------+')

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

    def info_animo(self):
        self.ani_board.check()
        print('+----------------+')
        for key, val in self.ani_board.animo.items():
            print('| {:<10} : {} |'.format(key, val))
        print('+----------------+')




if __name__ == '__main__':
    jeu = Plateau()



    #jeu.ajoute_cache('x1', 'c1')
    #jeu.ajoute_cache('c2', 'x1')



