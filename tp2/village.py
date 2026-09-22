"""Exercices 2 -- Village"""

from habitant import Habitant

#- Ici ajout_habitant_composition est crée un habitant à l'intérieur de la classe Village,
#liant ainsi leur existance (composition)
#- A l'inverse, ajouter_habitant_agregation utilise un habitant indépendant au village,
#et pouvant donc être utilise dans d'autre village (agregation)

class Village():
    '''Classe village'''

    def __init__(self, nom):
        self.nom = nom
        self.habitants = []

    def get_habitants(self):
        '''Return la liste des habitants'''
        return self.habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        '''Ajoute un habitant par composition'''
        habitant = Habitant(nom, age, adresse, animaux)
        self.habitants.append(habitant)

    def ajouter_habitant_agregation(self, habitant):
        '''Ajoute un habitant par agregation'''
        self.habitants.append(habitant)

    def afficher_habitants(self):
        '''Affiche la liste des habitants'''
        for h in self.habitants:
            print(h)


pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
