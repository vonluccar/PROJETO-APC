import plotly.express as px
import pandas as pd
df=pd.read_csv("mapa.csv",engine='python')

fig = px.scatter_geo(df,animation_frame='ano',locations='iso',color="Pais",hover_name='Pais',size='medalhas',
                     projection="natural earth",title=str(object=" Medalhas acumuladas por país no mapa"))
fig.show()  