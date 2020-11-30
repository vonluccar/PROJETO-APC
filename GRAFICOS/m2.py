import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

ps=pd.read_csv('../DATA/Pasta1.csv', encoding='UTF-8', sep=';')
app = dash.Dash(__name__)
o=0
pt=ps[ps['países']==2004]

for i in ps['países']:
    w=len(ps[ps['países']==i])
    print(i)
    if w<5:
        ps=ps.drop(ps.loc[ps['países']==i].index)
print(ps)

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
    if yearslider==2016:
        dff = ps[ps['ano']==yearslider]
        for i in dff:
            if i==drop:
                dff=dff[dff['países']==i]
        print(dff)

        if len(dff)==1:
            piechart=px.pie(dff, labels=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

            return (piechart)

    if yearslider==2012:
        dff = ps[ps['ano']==yearslider]
        for i in dff:
            if i==drop:
                dff=dff[dff['países']==i]
        print(dff)

        if len(dff)==1:
            piechart=px.pie(dff, labels=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

            return (piechart)

    if yearslider==2008:
        dff = ps[ps['ano']==yearslider]
        for i in dff:
            if i==drop:
                dff=dff[dff['países']==i]
        print(dff)

        if len(dff)==1:
            piechart=px.pie(dff, labels=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

            return (piechart)

    if yearslider==2004:
        dff = ps[ps['ano']==yearslider]
        for i in dff:
            if i==drop:
                dff=dff[dff['países']==i]
        print(dff)
        
        if len(dff)==1:
            piechart=px.pie(dff, labels=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

            return (piechart)

    if yearslider==2000:
        dff = ps[ps['ano']==yearslider]
        for i in dff:
            if i==drop:
                dff=dff[dff['países']==i]
        print(dff)
        if len(dff)==1:
            piechart=px.pie(dff, labels=['ouro','prata','broze'], values=[dff['ouro'],dff['prata'],dff['bronze']])

            return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)
    