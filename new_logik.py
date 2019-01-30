# -*-encoding:Utf-8 -*

class Cadre():
    theme = [None, "salamandre", "grenouille", "poisson", "lezard", "tortue"]
    def __init__(self,liste):
        self.liste = [Cadre.theme[x] for x in liste]
        self.term_affiche(self.liste)

        pass

    def term_affiche(self,liste, titre=" "):
        print(titre)
        print("+--------------+--------------+")
        print("|{:^14}|{:^14}|".format(liste[0], liste[1]))
        print("|--------------+--------------|")
        print("|{:^29}|".format(liste[2]))
        print("|--------------+--------------|")
        print("|{:^14}|{:^14}|".format(liste[3], liste[4]))
        print("+--------------+--------------+")

if __name__ == '__main__':
    cadre1 = Cadre([1,2,3,4,5])

