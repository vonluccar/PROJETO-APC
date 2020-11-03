import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from grafico_do_pib import pib
import grafico_de_medalhas_por_paises
from gráfico_map import mapa


app = dash.Dash()

app.layout = html.Div([
            html.Div(
            dcc.Graph(
                figure=pib()
            ), style={'marginTop':180},),

            html.Div(
                dcc.Graph(
                    figure=mapa()
                ), style={'marginTop':180})
                
    ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)

    

