"""Exercices 9 -- Test"""

import unittest
from habitant import *

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

if __name__ == "__main__":
    unittest.main(verbosity=2)