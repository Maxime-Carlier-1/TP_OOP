"""Exercices 6 -- Qualité de code"""

def cout_deplacement_propre(terrain, x1, y1, x2, y2):
    """Calcul le cout energetique d'un deplacement"""
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if terrain == "R":
        c = distance * 1.0
    elif terrain == "H":
        c = distance * 1.5
    elif terrain == "S":
        c = distance * 2.0
    else:
        c = distance * 3.0
    return c
