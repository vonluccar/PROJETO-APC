import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

ps=pd.read_csv('data/Pasta1.csv', encoding='UTF-8', sep=';') #Importação do arquivo csv
app = dash.Dash(__name__)

#Retira países com baixo desempenho nas 5 olímpiadas analisadas:
for i in ps['países']:
    w=len(ps[ps['países']==i])
    if w<5:
        ps=ps.drop(ps.loc[ps['países']==i].index)

#Cria lista com países que tiveram desempenho satisfatório:
available_indicators = ps['países'].unique()


#Plotagem do Dropdownd e do App
app.layout=html.Div([
    html.Label(['Número de Medalhas por Países']),
    dcc.Dropdown(
        id='drop',
        options=[
                 {'label': i, 'value': i} for i in available_indicators], #Percorre todos os países avaliados e os utiliza como parametro no Dropdown

        value=['ouro','prata','bronze'],
        style={"width": "50%"}
    ),
    dcc.Dropdown(
        id='yearslider',
        options=[
            {'label': year, 'value': year} for year in ps['ano'].unique() #Cria o Dropdown que possibilita a escolha do ano
            ],
        value='ano',
        style={"width": "50%"}
    ),

    html.Div([
    dcc.Graph(id='the_chart')
])
])

#Plotagem do callback
@app.callback(
    Output(component_id='the_chart', component_property='figure'),
    Input(component_id='drop', component_property='value'),
    Input(component_id='yearslider', component_property='value'),
)


#Função que gera o grafico:
def generate_chart(drop, yearslider):
    dff = ps
    e=[]

    #Une todos os países do csv em uma única lista
    for i in ps['países']:
        e.append(i)
    #Se o ano selecionado no Dropdown estiver na lista ele ira utilizar apenas este ano como parametro (Restringe o ano de análise)
    if yearslider in [2000,2004,2008,2012,2016]:
        dff = ps[ps['ano']==yearslider]
    ##Se o país selecionado no Dropdown estiver na lista ele ira utilizar apenas este país como parametro (Restringe o país de análise)
    if drop in e:
        dff = dff[dff['países']==drop]


    medalhas=['Ouro','Prata','Bronze']
    #Plotagem do grafico:
    fig = go.Figure(data=[go.Bar(y=(dff['ouro']),name='Ouro'),
                          go.Bar(y=(dff['prata']),name='Prata'),
                          go.Bar(y=(dff['bronze']),name='Bronze')])
    fig.update_layout(barmode='group')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)