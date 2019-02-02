# -*-encoding:Utf-8 -*

""" interface en ligne de commandes pour jeu 'aqua' """
while True:
    ordre = input('?').split(' ')

    if len(ordre) == 1:
        if ordre[0] == '':
            pass
        else:
            print(' tu veux {}?'.format(ordre[0]))
    elif len(ordre) == 2:
        print(' tu veux {} et {}?'.format(ordre[0], ordre[1]))
    elif len(ordre) == 3:
        print(' tu veux {} et {} et {}?'.format(ordre[0], ordre[1], ordre[2]))
    elif len(ordre) >= 4:
        print ("trop d'arguments")