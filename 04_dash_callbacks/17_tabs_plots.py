import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H2('Dash Tab Template'),

    dcc.Tabs(
        id='tabs-1',
        children=[
            dcc.Tab(label='Bar plot', value='tab-1'),
            dcc.Tab(label='Line plot', value='tab-2'),
            dcc.Tab(label='Scatter plot', value='tab-3')
        ],
        value='tab-1'
    ),

    html.Div(id='div-1')
])
@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Bar plot'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3],
                         'y': [1, 3, 4],
                         'type': 'bar'}
                    ]
                }
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Line plot'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 5],
                         'y': [1, 3, 4, 2],
                         'type': 'line'}
                    ]
                }
            )
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Scatter plot'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 6, 4],
                         'y': [1, 3, 4, 4, 3],
                         'mode': 'markers'}
                    ]
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
