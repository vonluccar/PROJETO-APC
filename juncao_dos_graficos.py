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
        ), style={'marginTop':180},),

        html.Div(
            dcc.Graph(
                figure=pib()
            ), style={'marginTop':180}),

        html.Div(
            dcc.Graph(
                figure=potencial_de_investimento()
            ), style={'marginTop':500},
        ),

    html.Div([
        html.Label(['Número de Medalhas por Países']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ano 2000', 'value': 'Total de Medalhas 2000'},
                     {'label': 'Ano 2004', 'value': 'Total de Medalhas 2004'},
                     {'label': 'Ano 2008', 'value': 'Total de Medalhas 2008'},
                     {'label': 'Ano 2012', 'value': 'Total de Medalhas 2012'},
                     {'label': 'Ano 2016', 'value': 'Total de Medalhas 2016'},
            ],
            value='Total de Medalhas 2000',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),
    
    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    
])

@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)

if __name__ == '__main__':
    app.run_server(debug=True)