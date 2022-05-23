import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H2(children='Hello Dash!'),

    html.Div(children='To moja pierwsza alplikacja w pythonie'),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=[1, 2, 3],
                y=[2, 1, 4]
            )
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
