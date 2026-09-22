"""Exercices 1 -- Habitant"""

class Habitant():
    '''Classe habitant'''

    def __init__(self, nom, age, adresse, animaux=None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    def get_nom(self):
        '''Return le nom de l'habitant'''
        return self.__nom

    def get_age(self):
        '''Return l'âge de l'habitant'''
        return self.__age

    def get_adresse(self):
        '''Return l'adresse de l'habitant'''
        return self.__adresse

    def get_animaux(self):
        '''Return les animaux de l'habitant'''
        return self.__animaux

    def set_nom(self, nom):
        '''Set le nom de l'habitant'''
        self.__nom = nom

    def set_age(self, age):
        '''Set l'age de l'habitant'''
        self.__age = age

    def set_adresse(self, adresse):
        '''Set l'adresse de l'habitant'''
        self.__adresse = adresse

    def set_animaux(self, animaux):
        '''Set les animaux de l'habitant'''
        self.__animaux = animaux

    def affichage_adresse(self):
        '''Affiche l'adresse de l'habitant'''
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self, animal):
        '''Return le compte des animaux (0 si l'animal n'existe pas)'''
        return self.__animaux.get(animal, 0)
