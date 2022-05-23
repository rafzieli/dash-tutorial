import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div(
        'Przykladowa sekcja',
        style={
            'color': 'darkblue',
            'fontSize': 18,
            'background-color': 'lightblue',
            'text-align':'center',
            'border': '4px solid Grey',
            'border-style': 'dashed'
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
