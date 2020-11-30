import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

ps=pd.read_csv('../data/Pasta1.csv', encoding='UTF-8', sep=';')
app = dash.Dash(__name__)
ps.head()
print(ps.loc[1])
o=[]
p=[]
b=[]
y=0

for i in ps:
    o.append(ps.loc[y, 'ouro'])
    p.append(ps.loc[y, 'prata'])
    b.append(ps.loc[y, 'bronze'])
    y+=1

h=0
for i in o:
    o[h]=str(o[h])
    p[h]=str(p[h])
    b[h]=str(b[h])
    h+=1

print(o)

app.layout=html.Div([
    html.Label(['Número de Medalhas por Países']),
    dcc.Dropdown(
        id='drop',
        options=[
                 {'label': str(ps.loc[i, "países"]), 'value': str(ps.loc[i, ["ouro", "prata", "bronze"]])} for i in range(len(ps))],

        value='ouro',
        multi=False,
        clearable=False,
        style={"width": "50%"}
    ),
    
    html.Div([
    dcc.Graph(id='graph')
])
])
    

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='drop', component_property='value')],
)

def update_ograf(drop):
    dff = ps

    piechart=px.pie(
            data_frame=dff,
            names=drop,
            hole=.3,
            )

    return (piechart)

if __name__ == '__main__':
    app.run_server(debug=True)