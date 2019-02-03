# -*-encoding:Utf-8 -*

""" interface en ligne de commandes pour jeu 'aqua' """
commande = {'HELP': [0,"tu veux de l'aide"],
            'ADD': [2,'tu veux ajouter un cadre'],
            'REMOVE': [1,'tu veux enleverr un cadre'],
            'ROTATE': [2,'tu veux tourner un cadre'],
            'INFO':[0,'tu veux des infos'],
            }
while True:
    ordre = input('Que veux tu faire ?').upper().split(' ')
    if len(ordre) == 1 and ordre[0] == '':
            pass
    if len(ordre) >=1 and len(ordre) < 4:
        if ordre[0] not in commande.keys():
            print("j'ai pas compris...{}".format(ordre[0]))
        else:
            print("{}".format(commande[ordre[0]][1]))
    else:
        print('ya trop de mots là...')

