import jupyter
import plotly.graph_objects as go
from plotly import colors

#Definição do grafico como uma função para importamos posteriormente
def pib():
    PIB = ['AUSTRALIA', 'BRASIL','CANADA', 'ESTADOS UNIDOS', 'CHINA', 'JAPÃO','AFRICA DO SUL','ITÁLIA','FRANÇA','INGLATERRA','ALEMANHA','QUÊNIA,',
                                                                                                                               'RUSSIA','CUBA','ARGENTINA','GRECIA'] #Definição da lista de todos os países que vão ter o PIB analisado
    # Plotagem do grafico de barra:
    fig = go.Figure(data=[
        go.Bar(name='2000', x=PIB, y=[0.41, 0.65, 0.74, 10.25, 1.21, 4.88, 0.13, 1.14, 1.36, 1.65, 1.94, 0.01, 0.25, 0.03, 0.28,0.13], marker_color='#FDC132'), #O eixo X recebe a lista dos países enquanto o Y recebe o PIB dos países em determinado ano (na casa do trilhão)/ name informa o ano analisado
        go.Bar(name='2004', x=PIB, y=[0.61, 0.67, 1.02, 12.21, 1.95, 4.81, 0.22, 1.80, 2.11, 2.41, 2.8, 0.01, 0.59, 0.03, 0.16,0.24], marker_color='#9B51E0'),  #O eixo X recebe a lista dos países enquanto o Y recebe o PIB dos países em determinado ano (na casa do trilhão)/ name informa o ano analisado
        go.Bar(name='2008', x=PIB, y=[1.05, 1.7, 1.54, 14.71, 4.59, 5.03, 0.286, 2.39, 2.91, 2.92, 3.73, 0.03, 1.66, 0.06, 0.36,0.35], marker_color='#EB5757'), #O eixo X recebe a lista dos países enquanto o Y recebe o PIB dos países em determinado ano (na casa do trilhão)/ name informa o ano analisado
        go.Bar(name='2012', x=PIB, y=[1.54, 2.4, 1.82, 16.20, 8.53, 6.20, 0.39, 2.08, 2.68, 2.70, 3.52, 0.05, 2.21, 0.07, 0.54,0.24], marker_color='#38C976'),  #O eixo X recebe a lista dos países enquanto o Y recebe o PIB dos países em determinado ano (na casa do trilhão)/ name informa o ano analisado
        go.Bar(name='2016', x=PIB, y=[1.20, 1.8, 1.52, 18.71, 11.14, 4.93, 0.26, 1.87, 2.47, 2.62, 3.46, 0.06, 1.28, 0.09, 0.55,0.19], marker_color='#2D9CDB'), #O eixo X recebe a lista dos países enquanto o Y recebe o PIB dos países em determinado ano (na casa do trilhão)/ name informa o ano analisado
    ])

    fig.update_layout(barmode='group',title=str(object="PIB's dos Países em Unidade de Trilhão")) #Atualização do design do grafico: Barmode se refere a como as barras vão se comportar/Title define o Título do grafico
    
    return fig
pib()
