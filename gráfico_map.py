#!/usr/bin/env python
# -- coding: utf-8 --
import plotly.express as px
import pandas as pd
def mapa():
    df=pd.read_csv("mapa.csv",engine='python',encoding = "utf-8")

    fig = px.scatter_geo(df,animation_frame='ano',locations='iso',color="Pais",hover_name='Pais',size='medalhas',size_max=int(40),
                        projection="natural earth",title=str(object=" Medalhas Acumuladas por País no Mapa"))

    fig.update_yaxes(automargin=True)
    fig.update_layout(height=1300, margin={"r": 0, "t": 0, "l": 50, "b": 0})
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig
mapa()
