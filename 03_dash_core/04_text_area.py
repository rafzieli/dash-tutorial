import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Textarea(
        placeholder='Wprowadz watrosc',
        style={'width': '100%'},
        value=''
    ),

    dcc.Textarea(
        placeholder='Wprowadz watrosc',
        style={'width': '60%'}
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
