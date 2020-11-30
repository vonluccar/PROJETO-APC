import plotly.graph_objects as px 
import numpy as np
import plotly.graph_objects as go


#Definição do grafico como uma função para importamos posteriormente
def potencial_de_investimento():
	x = ['Australia', 'Canada', 'Brasil', 'Estados Unidos', 'China', 'Japão', 'Africa do Sul', 'Itália', 'França',
		 'Inglaterra', 'Alemanha', 'Quênia', 'Russia', 'Cuba', 'Argentina','Grecia']  #Definição da lista dos países a serem analisados

	plot = px.Figure(data=[go.Bar(
		name='2000', #Ano da analise
		y=x, #Inversão dos eixos para estilização do grafico
		x=[141.4, 18.9, 18.4, 9, 47.9, 3.6, 38.4, 29.8, 27.9, 16.9, 17, 583, 356, 996, 14,100], marker_color='#FDC132', #Divisão do número pelo PIB (Na casa de trilhão)
		orientation='h' #Orientação da barra
	),
		go.Bar(
			name='2004', #Ano da analise
			y=x, #Inversão dos eixos para estilização do grafico
			x=[81.9, 11.7, 15.15, 8.27, 32.3, 7.9, 27.27, 19.77, 15.63, 12.44, 17.5, 437.5, 166.66, 900, 37.5,66.7], #Divisão do número pelo PIB (Na casa de trilhão)
			marker_color='#9B51E0',
			orientation='h' #Orientação da barra
		), go.Bar(
			name='2008', #Ano da analise
			y=x, #Inversão dos eixos para estilização do grafico
			x=[43.8, 12.3, 9.3, 7.47, 21.78, 4.97, 3.49, 11.29, 14, 16.09, 10.9, 233.33, 43.97, 866.6, 16.66,11.5], #Divisão do número pelo PIB (Na casa de trilhão)
			marker_color='#EB5757',
			orientation='h'), #Orientação da barra

		go.Bar(
			name='2012', #Ano da analise
			y=x, #Inversão dos eixos para estilização do grafico
			x=[22.72, 9.8, 6.9, 6.41, 10.31, 6.1, 15.3, 11.5, 12.6, 24.07, 12.5, 220, 37.1, 200, 7.4,8.4], #Divisão do número pelo PIB (Na casa de trilhão)
			marker_color='#38C976',
			orientation='h'), #Orientação da barra
		go.Bar(
			name='2016', #Ano da analise
			y=x, #Inversão dos eixos para estilização do grafico
			x=[24.16, 14.47, 11.1, 6.46, 6.28, 8.31, 38.46, 14.9, 17, 25.5, 12.13, 188.4, 43.75, 120.8, 7.2,31.5], #Divisão do número pelo PIB (Na casa de trilhão)
			marker_color='#2D9CDB',
			orientation='h') #Orientação da barra
	])




	# Plotagem dos botões (Dropdown)
	plot.update_layout(
		updatemenus=[
			dict(
				type="buttons",
				direction="left",
				buttons=list([
					dict(label="Potencial de Investimento", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [True, True, True, True, True]}, #Visibilidade das barras de cada ano
							   {"title": "Potencial de Investimento	"}]), #Titulo que surge ao selecionar o Botão
					dict(label="2000", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [True, False, False, False, False]}, #Visibilidade das barras de cada ano
							   {"title": "Medalha por PIB no Ano 2000", #Titulo que surge ao selecionar o Botão
								}]),
					dict(label="2004", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [False, True, False, False, False]}, #Visibilidade das barras de cada ano
							   {"title": "Medalha por PIB no Ano 2004", #Titulo que surge ao selecionar o Botão
								}]),
					dict(label="2008", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [False, False, True, False, False]}, #Visibilidade das barras de cada ano
							   {"title": "Medalha por PIB no Ano 2008", #Titulo que surge ao selecionar o Botão
								}]),
					dict(label="2012", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [False, False, False, True, False]}, #Visibilidade das barras de cada ano
							   {"title": "Medalha por PIB no Ano 2012", #Titulo que surge ao selecionar o Botão
								}]),
					dict(label="2016", #Titulo do botão
						 method="update", #Método de atualização das informações
						 args=[{"visible": [False, False, False, False, True]}, #Visibilidade das barras de cada ano
							   {"title": "Medalha por PIB no Ano 2016", #Titulo que surge ao selecionar o Botão
								}]),
				]),
			)
		],title=str(object="Potencial de Investimento")) #Titulo inicial do grafico

	return plot

potencial_de_investimento()
