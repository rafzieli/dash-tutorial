import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Input(
        type='text'
    ),

    html.Br(),

    dcc.Input(
        type='text',
       placeholder='Wprowadz tekst'
    ),

    dcc.Input(
        type='number',
        placeholder='Wprowadz liczbe'
    ),

    html.Br(),

    dcc.Input(
        type='password',
        placeholder='Wprowadz haslo'
    ),

    dcc.Input(
        type='email',
        placeholder='Wprowadz email'
    ),

    html.Br(),

])

if __name__ == '__main__':
    app.run_server(debug=True)
