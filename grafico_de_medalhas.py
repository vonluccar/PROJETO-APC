import plotly.graph_objects as px 
import numpy as np
import plotly.graph_objects as go


x = ['Australia', 'Canada','Brasil', 'Estados Unidos', 'China', 'Japão','Africa do Sul','Itália','França','Inglaterra','Alemanha','Quênia,','Russia','Cuba','Argentina'] 

plot = px.Figure(data=[go.Bar( 
	name='2000', 
	x=x, 
	y=[ , , , , , , , , , , , , , , ], marker_color='#FDC132',
    orientation = 'v'
), 
	go.Bar( 
	name='2004', 
	x=x, 
	y=[ , , , , , , , , , , , , , , ], marker_color='#9B51E0' ,
    orientation = 'v'
), go.Bar( 
	name='2008',
	x=x, 
	y=[ , , , , , , , , , , , , , , ], marker_color='#EB5757' ,
    orientation = 'v'),

     go.Bar( 
	name='2012',
	x=x, 
	y=[ , , , , , , , , , , , , , , ], marker_color='#38C976' ,
    orientation = 'v'),
     go.Bar( 
	name='2016',
	x=x, 
	y=[ , , , , , , , , , , , , , , ], marker_color='#2D9CDB' ,
    orientation = 'v')
]) 


# Add dropdown 
plot.update_layout( 
	updatemenus=[ 
		dict( 
			type="buttons", 
			direction="left", 
			buttons=list([ 
				dict(label="Número de Medalhas", 
					method="update", 
					args=[{"visible": [True,True,True,True,True]}, 
						{"title": "Número de Medalhas"}]), 
				dict(label="2000", 
					method="update", 
					args=[{"visible": [True, False,False,False,False]}, 
						{"title": "Medalhas Total no Ano 2000", 
							}]), 
				dict(label="2004", 
					method="update", 
					args=[{"visible": [False, True,False,False,False]}, 
						{"title": "Medalhas Total no Ano 2004", 
							}]), 
                dict(label="2008", 
					method="update", 
					args=[{"visible": [False,False,True,False,False]}, 
						{"title": "Medalhas Total no Ano 2008", 
							}]), 
                dict(label="2012", 
					method="update", 
					args=[{"visible": [False,False,False,True,False]}, 
						{"title": "Medalhas Total no Ano 2012", 
							}]), 
                dict(label="2016", 
					method="update", 
					args=[{"visible": [False,False,False,False,True]}, 
						{"title": "Medalhas Total no Ano 2016", 
							}]), 
			]), 
		) 
	]) 

plot.show() 