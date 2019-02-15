    def term_affiche(self):
        print (self.pos)
        print("+---+")
        print('|{} {}|'.format(self.liste_current[0], self.liste_current[1]))
        print('| {} |'.format(self.liste_current[2]))
        print('|{} {}|'.format(self.liste_current[3], self.liste_current[4]))
        print("+---+")

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
        self.animals = {x: 0 for x in Cadre.theme if x is not ''}
        self.board = {self.cadre1.nom: self.cadre1,
                      self.cadre2.nom: self.cadre2,
                      self.cadre3.nom: self.cadre3,
                      self.cadre4.nom: self.cadre4,
                      self.cache1.nom: self.cache1,
                      self.cache2.nom: self.cache2,
                      self.cache3.nom: self.cache3,
                      self.cache4.nom: self.cache4,
                      }
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
        new_l_cache = [self.board[x].nom for x in self.board.keys() if self.board[x].nom[0] == 'x' ]
        dispo = ''
        for elem in l_cache:
            dispo += elem + ' '
        print('+'+len(l_cache)*8*'-'+'---------+')
        print('| dispo: {} |'.format(dispo))
        print('+' + len(l_cache) * 8 * '-' + '---------+')
        print('new:{}'.format(new_l_cache))

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





