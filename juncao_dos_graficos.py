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
import base64

df = pd.read_csv("numero_de_medalhas.csv")
app = dash.Dash(__name__)
image_filename = 'arcos_olimpicos.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([

        html.Div(
            [
                html.H1(children='Dados para Investimentos em Esportes Olímpicos',
                        className='ten columns'),
                html.Img(
                    src='data:image/png;base64,{}'.format(encoded_image.decode()),
                    className='three columns',
                    style={
                        'height': '15%',
                        'width': '15%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),]
        ),

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
            ), style={'marginTop':180},
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