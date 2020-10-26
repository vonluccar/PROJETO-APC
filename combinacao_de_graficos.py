import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px

df = px.data.gapminder()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df.country.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,
                  config={
                      'staticPlot': True,
                      'scrollZoom': True,
                      'doubleClick': 'reset',
                      'showTips': True,
                      'displayModeBar': True,
                      'watermark': True,

                        },
                  className='six columns'
                  )
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(data_gapminder):
    df = px.data.gapminder()
    fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection="natural earth")
    return fig


@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:

        fig2 = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection="natural earth")
        return fig2
    else:
        print(f'hover data: {hov_data}')
        dff2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection="natural earth")
        return fig2


if __name__ == '__main__':
    app.run_server(debug=True)