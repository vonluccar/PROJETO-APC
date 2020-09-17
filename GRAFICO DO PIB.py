import jupyter
import plotly.graph_objects as go
from plotly import colors

PIB = ['AUSTRALIA', 'CANADA', 'ESTADOS UNIDOS', 'CHINA', 'JAPÃO','AFRICA DO SUL','ITÁLIA','FRANÇA','INGLATERRA','ALEMANHA','QUÊNIA',
                                                                                                                           'RUSSIA','CUBA','ARGENTINA']

fig = go.Figure(data=[
    go.Bar(name='2000', x=PIB, y=[20, 14, 23, 34 , 44, 23, 32, 43, 21, 12, 11, 12, 13, 14], marker_color='#FDC132'),
    go.Bar(name='2004', x=PIB, y=[12, 18, 29, 44, 54, 12, 32, 43, 12, 43, 54, 76, 31, 43], marker_color='#9B51E0'),
    go.Bar(name='2008', x=PIB, y=[20, 14, 23, 45, 54, 32, 54, 23, 43, 21, 23, 43, 56, 65], marker_color='#EB5757'),
    go.Bar(name='2012', x=PIB, y=[12, 18, 29, 32, 23, 76, 64, 67, 42, 65, 31, 54, 64, 67], marker_color='#38C976'),
    go.Bar(name='2016', x=PIB, y=[12, 18, 29, 21, 43, 65, 76, 53, 32, 67, 12, 87, 12, 54], marker_color='#2D9CDB'),
])
# Change the bar mode

fig.update_layout(barmode='group')
fig.show()
