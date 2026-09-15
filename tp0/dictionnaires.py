"""Exercices 5 -- Inventaire de pieces"""

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock,modele,piece):
    """Return le nombre de piece d'un modele"""
    return stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(stock,modele,piece,nbr):
    """Update le dictionnaire après l'utilisation d'une piece"""
    stock[modele][piece] -= nbr

def ajouter_modele(stock,modele,moteurs,capteurs,roues):
    """Update le dictionnaire après l'ajout d'un modele"""
    stock[modele] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}

def total_pieces(stock):
    """Return le nombre total de piece independemant du modele"""
    result = {"moteurs": 0, "capteurs": 0, "roues": 0}
    for modele in stock:
        for piece in stock[modele]:
            result[piece] += stock[modele][piece]
    return result

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
