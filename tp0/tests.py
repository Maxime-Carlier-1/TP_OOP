"""Exercices 7 -- Test unitaires"""

import unittest
from tuples import recalibrer, releves
from ensembles import robots_exploration, robots_transport
from ensembles import robots_double_mission, ajouter_robot_mission
from dictionnaires import consommer_piece, total_pieces, pieces_stock

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les releves (tuples)."""

    def test_recalibrer_capteur_existant(self):
        """Test la fonction recalibrer avec un capteur existant"""
        liste = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(liste[0],("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        """Test la fonction recalibrer dans le cas limite ou le capteur n'existe pas"""
        liste = recalibrer(releves, "laser_cote", 2.40)
        self.assertEqual(liste, releves)

class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les flottes de robots (ensembles)."""

    def test_robots_double_mission(self):
        """Test la fonction robots_double_mission"""
        resultat = robots_double_mission(robots_exploration, robots_transport)
        self.assertEqual(resultat, robots_exploration & robots_transport)

    def test_ajouter_robot_mission(self):
        """Test la fonction ajouter_robot_mission"""
        resultat = ajouter_robot_mission(robots_exploration, "R1")
        self.assertEqual(resultat, {"R2", "R5", "R7","R1"})

    def test_ajouter_robot_mission_deja_present(self):
        """Test la fonction ajouter_robot_mission"""
        resultat = ajouter_robot_mission(robots_exploration, "R5")
        self.assertEqual(resultat, robots_exploration)

class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions de l'inventaire (dictionnaires)."""

    def test_consommer_piece(self):
        """Test la fonction consommer_piece"""
        consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
        self.assertEqual(pieces_stock["ModeleA"]["moteurs"], 7)

    def test_total_pieces(self):
        """Test la fonction total_pieces"""
        resultat = total_pieces(pieces_stock)
        self.assertEqual(resultat, {"moteurs": 17, "capteurs": 50, "roues": 80})

    def test_total_pieces_sans_modele(self):
        """Test la fonction total_pieces dans le cas limite ou il n'y a pas de modele"""
        resultat = total_pieces({})
        self.assertEqual(resultat, {"moteurs": 0, "capteurs": 0, "roues": 0})

if __name__ == "__main__":
    unittest.main(verbosity=2)
