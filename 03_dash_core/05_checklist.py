import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ]
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        value=['py']
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        value=['py', 'sql']
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        value=['py', 'sql']
    ),

    html.Br()

])

if __name__ == '__main__':
    app.run_server(debug=True)
