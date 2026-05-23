import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_mock_data():
    """Charge les données mock depuis data/sample.csv"""
    path = os.path.join(BASE_DIR, "..", "data", "sample.csv")
    try:
        df = pd.read_csv(path)
        print(f"[OK] {len(df)} lignes chargées depuis sample.csv")
        return df
    except FileNotFoundError:
        print("[WARN] sample.csv introuvable, données de secours utilisées")
        return pd.DataFrame({
            "id": range(1, 11),
            "timestamp": [f"2026-05-01T10:{i*5:02d}:00" for i in range(10)],
            "valeur": [42.5, 38.1, 61.3, 29.7, 55.2, 47.8, 33.4, 50.0, 44.1, 27.3],
            "categorie": ["A","B","A","C","B","A","C","B","A","C"]
        })

def get_kpis(df):
    """Calcule les KPIs principaux"""
    return {
        "volume_total": len(df),
        "moyenne": round(df["valeur"].mean(), 2),
        "valeur_max": df["valeur"].max(),
        "nb_alertes": len(df[df["valeur"] > 55]),
        "distribution": df["categorie"].value_counts().to_dict()
    }

if __name__ == "__main__":
    df = load_mock_data()
    kpis = get_kpis(df)
    print("KPIs calculés :", kpis)