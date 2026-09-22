"""Exercices 1 -- Habitant"""

class Habitant():
    '''Classe habitant'''

    def __init__(self, nom, age, adresse, animaux=None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

    def affichage_adresse(self):
        '''Affche l'adresse de l'habitant'''
        print(f"{self.nom} habite a {self.adresse}")

    def compte_animal(self, animal):
        '''Return le compte des animaux (0 si l'animal n'existe pas)'''
        return self.animaux.get(animal, 0)


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
