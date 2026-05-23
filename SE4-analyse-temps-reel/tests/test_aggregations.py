from src.aggregations import moyenne_mobile, valeur_max, alerte

valeurs = [42.5, 38.1, 61.3, 29.7]

print("Moyenne :", moyenne_mobile(valeurs))   # attendu : 42.9
print("Max :", valeur_max(valeurs))            # attendu : 61.3
print("Alerte :", alerte(61.3))               # attendu : ALERTE
print("Pas alerte :", alerte(30))             # attendu : None