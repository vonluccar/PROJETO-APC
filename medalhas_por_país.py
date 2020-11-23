import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

arquivo = open('pasta1.csv', encoding='utf-8')
linhas = csv.reader(arquivo)
x=[]
for linha in linhas:
    x.append(linha)
print(x)

app = dash.Dash(__name__)

app.layout=html.Div([
    html.Label(['Número de Medalhas por Países']),
    dcc.Dropdown(
        id='drop',
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
    dcc.Graph(id='graph')
])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='drop', component_property='value')],
    [Input(component_id='', component_property='value')]
)

def update_ograf(drop):
    dff = arquivo

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)

if __name__ == '__main__':
    app.run_server(debug=True)