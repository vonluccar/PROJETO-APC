import plotly.graph_objects as go
import pandas as pd 
import xlrd


xlsx=pd.ExcelFile('medalhas_olimpiada2016.xlsx')
df = pd.read_excel(xlsx, 'medalhas_olimpiada2016')
x=df.loc[df['país']==input("sigla do país:")]

colors = ['#38C976', '#EB5757', '#2D9CDB']

fig = go.Figure(data=[go.Pie(labels=['Ouro', 'Prata', 'Bronze'],
                            values=[float(x['ouro']),float(x['prata']),float(x['bronze'])])])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.show()


