import plotly.graph_objects as px 
import numpy as np
import plotly.graph_objects as go



def potencial_de_investimento():
	x = ['Australia', 'Canada', 'Brasil', 'Estados Unidos', 'China', 'Japão', 'Africa do Sul', 'Itália', 'França',
		 'Inglaterra', 'Alemanha', 'Quênia', 'Russia', 'Cuba', 'Argentina','Grecia']

	plot = px.Figure(data=[go.Bar(
		name='2000',
		y=x,
		x=[141.4, 18.9, 18.4, 9, 47.9, 3.6, 38.4, 29.8, 27.9, 16.9, 17, 583, 356, 996, 14], marker_color='#FDC132',
		orientation='h'
	),
		go.Bar(
			name='2004',
			y=x,
			x=[81.9, 11.7, 15.15, 8.27, 32.3, 7.9, 27.27, 19.77, 15.63, 12.44, 17.5, 437.5, 166.66, 900, 37.5],
			marker_color='#9B51E0',
			orientation='h'
		), go.Bar(
			name='2008',
			y=x,
			x=[43.8, 12.3, 9.3, 7.47, 21.78, 4.97, 3.49, 11.29, 14, 16.09, 10.9, 233.33, 43.97, 866.6, 16.66],
			marker_color='#EB5757',
			orientation='h'),

		go.Bar(
			name='2012',
			y=x,
			x=[22.72, 9.8, 6.9, 6.41, 10.31, 6.1, 15.3, 11.5, 12.6, 24.07, 12.5, 220, 37.1, 200, 7.4],
			marker_color='#38C976',
			orientation='h'),
		go.Bar(
			name='2016',
			y=x,
			x=[24.16, 14.47, 11.1, 6.46, 6.28, 8.31, 38.46, 14.9, 17, 25.5, 12.13, 188.4, 43.75, 120.8, 7.2],
			marker_color='#2D9CDB',
			orientation='h')
	])




	# Add dropdown
	plot.update_layout(
		updatemenus=[
			dict(
				type="buttons",
				direction="left",
				buttons=list([
					dict(label="Potencial de Investimento",
						 method="update",
						 args=[{"visible": [True, True, True, True, True]},
							   {"title": "Potencial de Investimento	"}]),
					dict(label="2000",
						 method="update",
						 args=[{"visible": [True, False, False, False, False]},
							   {"title": "Medalha por PIB no Ano 2000",
								}]),
					dict(label="2004",
						 method="update",
						 args=[{"visible": [False, True, False, False, False]},
							   {"title": "Medalha por PIB no Ano 2004",
								}]),
					dict(label="2008",
						 method="update",
						 args=[{"visible": [False, False, True, False, False]},
							   {"title": "Medalha por PIB no Ano 2008",
								}]),
					dict(label="2012",
						 method="update",
						 args=[{"visible": [False, False, False, True, False]},
							   {"title": "Medalha por PIB no Ano 2012",
								}]),
					dict(label="2016",
						 method="update",
						 args=[{"visible": [False, False, False, False, True]},
							   {"title": "Medalha por PIB no Ano 2016",
								}]),
				]),
			)
		], height=800, title=str(object="Potencial de Investimento"))

	return plot

potencial_de_investimento()
