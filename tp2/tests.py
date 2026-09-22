"""Exercices 9 -- Test"""

import unittest
from habitant import *
from village import *

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""

    def test_age_setter_valide(self):
        habitant = Adulte("Alice", 30, "Rue C", None)
        self.assertEqual(habitant.age, 30)

    def test_age_setter_invalide(self):
        """Cas limite : age negatif."""
        with self.assertRaises(ValueError):
            habitant = Adulte("Lucie", -5, "Rue D", None)

    def test_comptage_animaux(self):
        habitant = Adulte("Alice", 30, "Rue C", {"vache": 2})
        self.assertEqual(habitant.get_animaux(), {"vache": 2})

    def test_comptage_animaux_invalide(self):
        """Cas limite : animal inexistant"""
        habitant = Adulte("Alice", 30, "Rue C", {"vache": 2})
        self.assertEqual(habitant.compte_animal("cheval"), 0)

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village et l’agregation/composition."""

    def test_composition_valide(self):
        village = Village("TestVillage")
        village.ajouter_habitant_composition("Bob", 40, "Rue E", None)
        #on compare les attributs ca rsi on crée un habitant par composition, il n'est pas accessible en dehors du village
        #et donc on ne peut pas le verifier dans assertEqual
        self.assertEqual(len(village.habitants), 1)
        self.assertEqual(village.habitants[0].get_nom(), "Bob")
        self.assertEqual(village.habitants[0].age, 40)
        self.assertEqual(village.habitants[0].get_adresse(), "Rue E")
        self.assertEqual(village.habitants[0].get_animaux(), {})

    def test_agregation_valide(self):
        village = Village("TestVillage")
        h = Adulte("Bob", 40, "Rue E", None)
        village.ajouter_habitant_agregation(h)
        self.assertEqual(village.habitants, [h])

    def test_agregation_partagee(self):
        village1 = Village("Village1")
        village2 = Village("Village2")
        h = Adulte("Bob", 40, "Rue E", None)
        village1.ajouter_habitant_agregation(h)
        village2.ajouter_habitant_agregation(h)
        self.assertIn(h, village1.habitants)
        self.assertIn(h, village2.habitants)

if __name__ == "__main__":
    unittest.main(verbosity=2)