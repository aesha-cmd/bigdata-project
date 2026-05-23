# Fonctions d'agrégation sur le stream
def moyenne_mobile(valeurs):
    return sum(valeurs) / len(valeurs)

def valeur_max(valeurs):
    return max(valeurs)

def alerte(valeur, seuil=60):
    if valeur > seuil:
        return f" ALERTE : valeur {valeur} dépasse le seuil {seuil}"
    return None