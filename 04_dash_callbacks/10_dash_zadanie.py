import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'Polska': ['Warszawa', 'Krakow', 'Wroclaw'],
    'Stany Zjednoczone': ['New York', 'Los Angeles']
}

app.layout = html.Div([

    dcc.RadioItems(id='radio-1',
                    options=[{'label': key, 'value': key} for key in all_options.keys()],
                    value='Polska'),

    html.Hr(),

    dcc.RadioItems(id='radio-2'),

    html.Hr(),

    html.Div(id='div-1')
])
@app.callback(
    [Output('radio-2', 'options'),
     Output('radio-2', 'value')],
    [Input('radio-1', 'value')]
)

def generate_radio_button(selected):
    return [{'label': key, 'value': key} for key in all_options[selected]], all_options[selected][0]

@app.callback(
    Output('div-1', 'children'),
    [Input('radio-1', 'value'),
     Input('radio-2', 'value')]
)

def test_generator(selected_1, selected_2):
    return f'Podales {selected_1} i {selected_2}.'

if __name__ == '__main__':
    app.run_server(debug=True)
