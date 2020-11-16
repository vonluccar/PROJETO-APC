import plotly.express as px
import pandas as pd
def mapa():
    df=pd.read_csv("mapa.csv",engine='python')

    fig = px.scatter_geo(df,animation_frame='ano',locations='iso',color="Pais",hover_name='Pais',size='medalhas',size_max=int(40),
                        projection="natural earth",title=str(object=" Medalhas Acumuladas por País no Mapa"),width=1300,height=760)

    fig.update_yaxes(automargin=True)
    return fig
mapa()