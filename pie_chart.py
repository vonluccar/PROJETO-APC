import plotly.graph_objects as go
colors = ['#38C976', '#EB5757', '#2D9CDB']

fig = go.Figure(data=[go.Pie(labels=['Ouro', 'Prata', 'Bronze'],
                             values=[46,37,38])])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.show()