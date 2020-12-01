import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

ps=pd.read_csv('data/pasta1.csv', encoding='UTF-8', sep=';')
app = dash.Dash(__name__)
o=0
pt=ps[ps['países']==2004]

for i in ps['países']:
    w=len(ps[ps['países']==i])
    if w<5:
        ps=ps.drop(ps.loc[ps['países']==i].index)

available_indicators = ps['países'].unique()

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
            {'label': year, 'value': year} for year in ps['ano'].unique()
            ],
        value='ano',
        style={"width": "50%"}
    ),

    html.Div([
    dcc.Graph(id='the_chart')
])
])


@app.callback(
    Output(component_id='the_chart', component_property='figure'),
    Input(component_id='drop', component_property='value'),
    Input(component_id='yearslider', component_property='value'),
)

def generate_chart(drop, yearslider):
    dff = ps
    e=[]
    for i in ps['países']:
        e.append(i)

    if yearslider in [2000,2004,2008,2012,2016]:
        dff = ps[ps['ano']==yearslider]

    if drop in e:
        dff = ps[ps['países']==drop]

    valor1 = dff['ouro']
    valor2 = dff['prata']
    valor3 = dff['bronze']

    fig = go.Figure(data=[go.Bar(y=[valor1,valor2,valor3], x=['ouro','prata','bronze'])])

    return (fig)


if __name__ == '__main__':
    app.run_server(debug=True)