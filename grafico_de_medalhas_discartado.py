import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from grafico_do_pib import pib
from gráfico_map import mapa
from grafico_de_potencial_de_investimento import potencial_de_investimento
import numpy as np

df = pd.read_csv("numero_de_medalhas.csv")
app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div(
        dcc.Graph(
            figure=mapa()
        ), style={'marginTop': 180}, ),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)