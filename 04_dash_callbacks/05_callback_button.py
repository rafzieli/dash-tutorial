import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
    dcc.Input(id='input-1', type='text')
    ]),

    html.Button(id='button-1', children='Submit', n_clicks=0),
    html.Div(id='div-1', children='Wprowadz tekst i przycisnij Submit')

])



@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='input-1', component_property='value'),
     Input(component_id='button-1', component_property='n_clicks')]
)
def update_output(value, n_clicks):
    return f'Wpisales {value} i wcisnales przycisk {n_clicks} razy.'


if __name__ == '__main__':
    app.run_server(debug=True)
