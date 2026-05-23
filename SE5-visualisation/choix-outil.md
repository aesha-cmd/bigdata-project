# Choix de l'outil BI

## Outil choisi : Dash (Plotly)

## Justification
- Open-source et 100% Python, cohérent avec notre stack Big Data
- Crée des dashboards web interactifs sans JavaScript
- S'intègre facilement avec Pandas, donc compatible SE2/SE3
- Déploiement local simple, pas besoin d'un serveur externe
- Le code est versionnable sur Git (contrairement à Power BI)

## Installation
```bash
pip install dash plotly pandas
```

## Lancement
```bash
python src/app.py
# Ouvre http://localhost:8050
```