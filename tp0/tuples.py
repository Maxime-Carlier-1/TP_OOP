"""Exercices 3 -- Tuples"""

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_relever(releve):
    """Afficher le releve sous forme de chaine de caracteres"""
    capteur, valeur, unite = releve
    return f"Capteur {capteur} : {valeur} {unite}"

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_relever(releve1) == "Capteur laser_avant : 2.35 m"

def recalibrer(list_releve,capteur,valeur):
    """Update la valeur de releves"""
    liste=[]
    for releve in list_releve :
        if releve[0] == capteur:
            liste.append((releve[0],valeur,releve[2]))
            continue
        liste.append(releve)
    return liste


nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
