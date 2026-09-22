"""Exercices 1 -- Habitant"""

class Habitant():
    '''Classe habitant'''

    def __init__(self, nom, age, adresse, animaux=None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

