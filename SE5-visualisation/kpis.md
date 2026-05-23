# KPIs — Dashboard Big Data Groupe 4

## Métriques affichées

1. **Volume total de données reçues** — nombre de lignes ingérées dans le pipeline
2. **Moyenne des valeurs** — moyenne arithmétique de la colonne `valeur`
3. **Valeur maximale détectée** — pic global détecté dans le flux
4. **Nombre d'alertes déclenchées** — lignes dont la valeur dépasse le seuil de 55
5. **Distribution par catégorie** — répartition des entrées A, B, C (graphique camembert)

## Seuil d'alerte
- Valeur > 55 → alerte déclenchée (point rouge sur le graphique)

## Source des données
- **S2** : données mock `data/sample.csv`
- **S3+** : données réelles issues du pipeline ETL de SE3