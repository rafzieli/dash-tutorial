import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table import FormatTemplate
import pandas as pd
import numpy as np
import pickle

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('./datasets/data_cleaned.csv', index_col=0)

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H3('Model Uczenia Maszynowego - Model regresyjny przewidywania ceny samochodow uzywanych'),
        html.H6('Model Lasow Losowych (biblioteka scikit - learn)')
    ], style={'text-align': 'center'}),
    html.Hr(),
    html.Div([
        html.Label('Podaj rok produkcji samochodu:'),
        dcc.Slider(
            id='slider-1',
            min=df.Year.min(),
            max=df.Year.max(),
            step=1,
            marks={i: str(i) for i in range(df.Year.min(), df.Year.max() + 1)}
        ),
        html.Hr(),
        html.Label('Podaj rozmiar silnika:'),
        dcc.Slider(
            id='slider-2',
            min=0,
            max=6000,
            step=1,
            marks={i: str(i) for i in range(0, 6001, 500)},
            tooltip={'placement': 'bottom'}
        ),
        html.Hr(),
        html.Label('Podaj moc auta:'),
        dcc.Slider(
            id='slider-3',
            min=30,
            max=580,
            step=1,
            marks={i: str(i) for i in range(30, 581, 50)},
            tooltip={'placement': 'bottom'}
        ),
    ], style={'width': '80%', 'text-align': 'left', 'margin': '0 auto', 'font-size': 22})
])

if __name__ == '__main__':
    app.run_server(debug=True)
