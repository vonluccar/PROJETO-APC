#!/usr/bin/env python
# -- coding: utf-8 --
import plotly.express as px
import pandas as pd

#Definição do grafico como uma função para importamos posteriormente
def mapa():
    df=pd.read_csv("data/mapa.csv", engine='python', encoding ="utf-8") #Importação do arquivo de dados/ Linguagem de codigo utilizada/ Formato de linguagem para a plotagem dos graficos

    fig = px.scatter_geo(df,animation_frame='ano',locations='iso',color="Pais",hover_name='Pais',size='medalhas',size_max=int(40), #Animation frame == define a linha do tempo e apresenta as anos que são utilizados no arquivo csv
                                                                                                                                   #Locations == Recebe a cigla do pais (ISO) e plota a bolha na localização do País
                                                                                                                                   #Color == Cada País recebe uma cor diferente
                                                                                                                                   #Hover name == Definição do nome de cada País na direita do mapa
                                                                                                                                   #Size == Tamanho da bolha será proporcional ao nome de Medalhas
                                                                                                                                   #Size Max == Tamanho maximo da bolha
                        projection="natural earth",title=str(object=" Medalhas Acumuladas por País no Mapa"))                      #Projection == Tipo de projeção do mapa
                                                                                                                                   #Title == Titulo do grafico
    fig.update_yaxes(automargin=True) #Definição da margem automaticamente
    fig.update_layout(height=1200)    #Tamanho do mapa
    fig.update_layout({               #Cor de fundo do grafico:
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig
mapa()
