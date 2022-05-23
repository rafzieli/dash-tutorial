import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'Language': ['Python', 'Sql', 'Java'],
    'Technology': ['Hadoop', 'Spark', 'Kafka']
}

app.layout = html.Div([

    dcc.RadioItems(
        id='radio-1',
        options=[{'label': key, 'value': key} for key in all_options.keys()],
        value='Language'
    ),

    html.Hr(),

    dcc.RadioItems(
        id='radio-2'
    ),

    html.Hr(),

    html.Div(id='div-1')

])

@app.callback(
    Output('radio-2', 'options'),
    [Input('radio-1', 'value')]
)

def set_options(selected_value):
    return [{'label': i, 'value': i} for i in all_options[selected_value]]

@app.callback(
    Output('div-1', 'children'),
    [Input('radio-1', 'value'),
     Input('radio-2', 'value')]
)

def update_div(selected_1, selected_2):
    return f'You choosed {selected_1} and {selected_2}.'

if __name__ == '__main__':
    app.run_server(debug=True)
