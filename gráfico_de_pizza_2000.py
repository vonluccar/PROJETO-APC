import plotly.graph_objects as go

labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
values = [12, 14, 97, 5, 34, 13, 18, 59, 58, 28, 56, 7, 88, 29, 4, 38]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
