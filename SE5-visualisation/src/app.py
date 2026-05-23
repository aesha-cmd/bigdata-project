import dash
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import os

app = dash.Dash(__name__)

# Chargement des données mock
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sample.csv")

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    df = pd.DataFrame({
        "id": range(1, 11),
        "timestamp": [f"2026-05-01T10:{i*5:02d}:00" for i in range(10)],
        "valeur": [42.5, 38.1, 61.3, 29.7, 55.2, 47.8, 33.4, 50.0, 44.1, 27.3],
        "categorie": ["A","B","A","C","B","A","C","B","A","C"]
    })

# KPIs
volume_total = len(df)
moyenne = round(df["valeur"].mean(), 2)
valeur_max = df["valeur"].max()
nb_alertes = len(df[df["valeur"] > 55])

card_style = {
    "padding": "20px",
    "borderRadius": "8px",
    "textAlign": "center",
    "flex": "1",
    "background": "#f5f5f5"
}

app.layout = html.Div([
    html.H1("Dashboard Big Data — Groupe 4",
            style={"textAlign": "center", "marginBottom": "30px", "marginTop": "20px"}),

    # KPI Cards
    html.Div([
        html.Div([html.P("Volume total"), html.H2(volume_total), html.Small("lignes reçues")], style={**card_style, "background":"#e8f0fe"}),
        html.Div([html.P("Moyenne"), html.H2(moyenne), html.Small("valeur moyenne")], style={**card_style, "background":"#e6f4ea"}),
        html.Div([html.P("Valeur max"), html.H2(valeur_max), html.Small("pic détecté")], style={**card_style, "background":"#fef3e2"}),
        html.Div([html.P("Alertes (> 55)"), html.H2(nb_alertes), html.Small("dépassements")], style={**card_style, "background":"#fce8e6"}),
    ], style={"display": "flex", "gap": "16px", "marginBottom": "30px", "padding": "0 20px"}),

    # Graphique 1 : ligne
    dcc.Graph(figure=go.Figure(
        data=[go.Scatter(
            x=df["timestamp"],
            y=df["valeur"],
            mode="lines+markers",
            name="Valeur",
            marker=dict(
                color=["red" if v > 55 else "#1a73e8" for v in df["valeur"]],
                size=8
            ),
            line=dict(color="#1a73e8", width=2)
        )],
        layout=go.Layout(
            title="Évolution des valeurs dans le temps",
            xaxis_title="Timestamp",
            yaxis_title="Valeur",
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
    )),

    # Graphique 2 : camembert
    dcc.Graph(figure=px.pie(
        df,
        names="categorie",
        title="Distribution par catégorie (A / B / C)",
        color_discrete_sequence=["#1a73e8", "#34a853", "#fbbc04"]
    )),

], style={"fontFamily": "Arial, sans-serif", "maxWidth": "1100px", "margin": "0 auto"})

if __name__ == "__main__":
    app.run(debug=True)