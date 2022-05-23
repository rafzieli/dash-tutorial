import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/dash_course/data.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Graph(id='graph-1'),
    dcc.Slider(
        id='slider-1',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        marks={str(year): str(year) for year in df.year.unique()},
        step=None
    )

])

@app.callback(
    Output('graph-1', 'figure'),
    [Input('slider-1', 'value')]
)

def update_graph(selected_year):
    dff=df[df['year'] == selected_year]
    traces = []
    for cont in df.continent.unique():
        dff_cont = dff[dff.continent == cont]
        traces.append(
            go.Scatter(
                x=dff_cont.gdpPercap,
                y=dff_cont.lifeExp,
                mode='markers',
                name=cont,
                opacity=0.6,
                marker={
                    'size': 15,
                    'line': {'width': 1.5, 'color': 'white'}
                },
                text=dff_cont['country']
            )
        )

    return {
        'data': traces,
        'layout': go.Layout(
            title_text='Wykres',
            xaxis={'type': 'log', 'title': 'PKB per capita'},
            yaxis={'title': 'Oczekiwana dlugosc zycia'},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)