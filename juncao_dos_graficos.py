import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from grafico_do_pib import pib
from gráfico_map import mapa
from grafico_de_potencial_de_investimento import potencial_de_investimento

df = pd.read_csv("data/numero_de_medalhas.csv") #Leitura do arquivo csv (DATA)

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

    #Estruturação do grafico de pizza (Problema do Callback)
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

])

#Callback (Atualização das informações em cada ano)
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'), ]
)
def update_graph(my_dropdown):
    dff = df

    piechart = px.pie(
        data_frame=dff,
        names=my_dropdown,
        hole=.3,
    )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)