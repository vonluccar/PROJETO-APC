import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import csv
from dash.dependencies import Input, Output
from grafico_do_pib import pib
from gráfico_map import mapa
from grafico_de_potencial_de_investimento import potencial_de_investimento

df = pd.read_csv("data/numero_de_medalhas.csv") #Leitura do arquivo csv (DATA)
ps=pd.read_csv('data/Pasta1.csv', encoding='UTF-8', sep=';') #Importação do arquivo csv


#Retira países com baixo desempenho nas 5 olímpiadas analisadas:
for i in ps['países']:
    w=len(ps[ps['países']==i])
    if w<5:
        ps=ps.drop(ps.loc[ps['países']==i].index)

#Cria lista com países que tiveram desempenho satisfatório:
available_indicators = ps['países'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([

    #Importação do Ícone
    html.Div([
        html.H2(""),
        html.Img(src="assets/icon.PNG")],
        className="banner"),

    # Importação do grafico do mapa:
    html.Div(
        dcc.Graph(
            figure=mapa()
        ), style={'marginTop': 180}, className="mapa"),

    # Importação do grafico do pib:
    html.Div(
        dcc.Graph(
            figure=pib()
        ), style={'marginTop': 180}, className="pib"),

    #Importação do grafico do potencial de investimento:
    html.Div(
        dcc.Graph(
            figure=potencial_de_investimento()
        ), style={'marginTop': 180}, className="Potencial"
    ),

    #Estruturação do grafico de pizza (Callback)
    html.Div([
        html.Label(['Número de Medalhas por Países']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                {'label': 'Ano 2000', 'value': 'Total de Medalhas 2000'}, #Definição do nome apresentado nos botões (Label)/ Dados apresentados obtidos pelo csv (value)
                {'label': 'Ano 2004', 'value': 'Total de Medalhas 2004'}, #Definição do nome apresentado nos botões (Label)/ Dados apresentados obtidos pelo csv (value)
                {'label': 'Ano 2008', 'value': 'Total de Medalhas 2008'}, #Definição do nome apresentado nos botões (Label)/ Dados apresentados obtidos pelo csv (value)
                {'label': 'Ano 2012', 'value': 'Total de Medalhas 2012'}, #Definição do nome apresentado nos botões (Label)/ Dados apresentados obtidos pelo csv (value)
                {'label': 'Ano 2016', 'value': 'Total de Medalhas 2016'}, #Definição do nome apresentado nos botões (Label)/ Dados apresentados obtidos pelo csv (value)
            ],
            value='Total de Medalhas 2000', #Importação do Dado advindo do csv
            style={"width": "50%"}, #Tamanho do grafico
        )
    ], style={'marginTop': 180}), #Distancia da margem do topo

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        html.Label(['Números e Tipos de Medalhas por País']),
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
    ]),
],style={'marginTop':180}),

])

#Callback (Atualização das informações em cada ano)
@app.callback(
    Output(component_id='the_graph', component_property='figure',),
    Input(component_id='my_dropdown', component_property='value'),
)

#Update do Gráfico de Pizza
def update_graph(my_dropdown):
    dff = df

    #Definições do Gráfico de Pizza
    piechart = px.pie(
        data_frame=dff,
        names=my_dropdown,
        hole=.3,
    )

    return (piechart)

@app.callback(
    Output(component_id='the_chart', component_property='figure'),
    Input(component_id='drop', component_property='value'),
    Input(component_id='yearslider', component_property='value'),
)
# Função que gera o grafico:
def generate_chart(drop, yearslider):
    dff = ps
    e = []

    # Une todos os países do csv em uma única lista
    for i in ps['países']:
        e.append(i)
    # Se o ano selecionado no Dropdown estiver na lista ele ira utilizar apenas este ano como parametro (Restringe o ano de análise)
    if yearslider in [2000, 2004, 2008, 2012, 2016]:
        dff = ps[ps['ano'] == yearslider]
    ##Se o país selecionado no Dropdown estiver na lista ele ira utilizar apenas este país como parametro (Restringe o país de análise)
    if drop in e:
        dff = dff[dff['países'] == drop]

    medalhas = ['Ouro', 'Prata', 'Bronze']
    # Plotagem do grafico:
    fig = go.Figure(data=[go.Bar(y=(dff['ouro']), name='Ouro'),
                          go.Bar(y=(dff['prata']), name='Prata'),
                          go.Bar(y=(dff['bronze']), name='Bronze')])
    fig.update_layout(barmode='group'),

    return fig

#Código do Dash (Responsável pelo server da página)
if __name__ == '__main__':
    app.run_server(debug=True)