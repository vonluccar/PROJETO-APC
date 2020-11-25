import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

ps=pd.read_csv('pasta1.csv', encoding='UTF-8', sep=';')
app = dash.Dash(__name__)
o=0
available_indicators = ps['países'].unique()
pt=ps[ps['países']==2004]


for i in ps['países']:
    w=len(ps[ps['países']==i])
    if w<5:
        ps=ps.drop(i)
print(ps)

app.layout=html.Div([
    html.Label(['Número de Medalhas por Países']),
    dcc.Dropdown(
        id='drop',
        options=[
                 {'label': i, 'value': i} for i in available_indicators],

        value=['ouro','prata','bronze'],
        style={"width": "50%"}
    ),
        dcc.Dropdown(
            id='yearslider',
            options=[
                {'label': year, 'value': year}for year in ps['ano'].unique()
                ],
            value='ano',
            style={"width": "50%"}
    ),
    
    html.Div([
    dcc.Graph(id='grap')
])
])
    

@app.callback(
    Output(component_id='grap', component_property='figure'),
    Input(component_id='drop', component_property='value'),
    Input(component_id='yearslider', component_property='value'),
)

def update_graph(drop, yearslider):
    dff = ps[ps['ano']==yearslider]
    dff = dff[dff['países']==drop]

    piechart=px.pie(dff, names=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

    return (piechart)

if __name__ == '__main__':
    app.run_server(debug=True)