# -*-encoding:Utf-8 -*
from new_logik import Cadre, Cache, Plateau

class Interpreteur():
    """ interface en ligne de commandes pour jeu 'aqua' """
    def __init__(self):
        self.commandes = {'HELP': [1, "tu veux de l'aide","pas d'arguments nécéssaire à cette fonction"],
                          'ADD': [3, 'tu veux ajouter un cache',"en arguments: cache (x1... x4) et cadre(c1... c4)"],
                          'REMOVE': [2, 'tu veux enlever un cache',"en arguments: le cache(x1... x4)"],
                          'ROTATE': [3, 'tu veux tourner un cache',"en arguments: le cache (x1... x4) et le sens de rotation ( H ou AH)"],
                          'INFO':[1, 'tu veux des infos'," en argument: tout, cache, cadre "],
                         }

    def aide(self):
        print("ceci est l'aide du jeu de la fonction")

    def check_valide(self, ordre):
        demande = [x for x in ordre if x != '' ]
        if demande == []:
            self.message_valide = ">pas d'arguments..."
            valide = False
        elif len(demande) > 3:
            self.message_valide = ">trop d'arguments..."
            valide = False
        else:
            if demande[0] not in self.commandes.keys():
                self.message_valide = '>je ne comprend pas...'
                valide = False
            elif len(demande)  > self.commandes[demande[0]][0]:
                self.message_valide = ">trop d'arguments pour {}".format(demande[0])
                valide = False
            elif len(demande)  < self.commandes[demande[0]][0]:
                self.message_valide = ">manque arguments pour {}".format(demande[0])
                valide = False
            else:
                valide = True
                self.message_valide = self.commandes[demande[0]][1]
        return valide

    def execute(self,ordre):
        print('>' + self.message_valide)
        if ordre[0] == 'HELP':
            self.aide()
        if ordre[0] == 'ADD':
            jeu.ajoute_cache(ordre[1].lower(),ordre[2].lower())
        if ordre[0] == 'REMOVE':
            jeu.enleve_cache(ordre[1].lower())
        if ordre[0] == 'INFO':
            jeu.info_board()


if __name__ == '__main__':
    jeu = Plateau()
    i = Interpreteur()

    while True:
        ordre = input('?').upper().split(' ')
        if i.check_valide(ordre):
            i.execute(ordre)
        else:
            print(i.message_valide)

