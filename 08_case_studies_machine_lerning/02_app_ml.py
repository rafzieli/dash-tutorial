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
        html.Br(),
        html.Label('Podaj liczbe pasazerow:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in [2, 4, 5, 6, 7, 8, 9, 10]]
            )
        ], style={'width': '20%', 'text-align': 'left'}),
        html.Br(),
        html.Label('Podaj typ paliwa:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': j} for i, j in zip(['Diesel', 'Benzyna', 'CNG', 'LPG', 'Elektryczny'],
                                                                  ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])]
            )
        ], style={'width': '20%', 'text-align': 'left'}),
        html.Br(),
        html.Label('Podaj typ przekladni:'),
        html.Div([
            dcc.RadioItems(
                id='radio-1',
                options=[{'label': i, 'value': j} for i, j in zip(['Manualna', 'Automatyczna'],
                                                                  ['Manual', 'Automatic'])]
            )
        ], style={'width': '20%', 'text-align': 'left'}),

        html.Div([
            html.Hr(),
            html.H3('Predykcja na podstawie modelu'),
            html.Hr(),
            html.H4('Podales parametry:'),
            html.Div(id='div-1'),
            html.Div(id='div-2'),
            html.Hr()
        ], style={'margin': '0 auto', 'text-align': 'center'})

    ], style={'width': '80%', 'text-align': 'left', 'margin': '0 auto', 'font-size': 22})
])

fuel_type = {'Diesel': 'Diesel', 'Petrol': 'Benzyna', 'CNG': 'CNG', 'LPG': 'LPG', 'Electric': 'Elektryczny'}
transmission = {'Manual': 'Manualna', 'Automatic': 'Automatyczna'}

@app.callback(
    Output('div-1', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('radio-1', 'value')]
)
def display_parameters(val1, val2, val3, val4, val5, val6):
    if val1 and val2 and val3 and val4 and val5 and val6:
        val5 = fuel_type[val5]
        val6 = transmission[val6]
        return html.Div([
            html.H6(f'Rok produkcji: {val1}'),
            html.H6(f'Pojemnosc silnika: {val2}'),
            html.H6(f'Moc silnika: {val3}'),
            html.H6(f'Liczba pasazerow: {val4}'),
            html.H6(f'Typ paliwa: {val5}'),
            html.H6(f'Typ przekladni: {val6}')
        ], style={'text-align': 'left'})
    else:
        return html.Div([
            html.H6('Podaj wszystkie parametry')
        ])
    print(val1, val2, val3, val4, val5, val6)

@app.callback(
    Output('div-2', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('radio-1', 'value')]
)
def predict_value(val1, val2, val3, val4, val5, val6):
    if val1 and val2 and val3 and val4 and val5 and val6:

        val5_1, val5_2, val5_3, val5_4 = 0, 0, 0, 0

        if val5 == 'Diesel':
            val5_1 = 1
        elif val5 == 'Electric':
            val5_2 = 1
        elif val5 == 'LPG':
            val5_3 = 1
        elif val5 == 'Petrol':
            val5_4 = 1

        if val6 == 'Manual':
            val6 = 1
        else:
            val6 = 0

        df_sample = pd.DataFrame(
            data=[
                [val1, val2, val3, val4, val5_1, val5_2, val5_3, val5_4, val6]
            ],
            columns=['Year', 'Engine', 'Power', 'Seats', 'Fuel_Type_Diesel', 'Fuel_Type_Electric',
                     'Fuel_Type_LPG', 'Fuel_Type_Petrol', 'Transmission_Manual']
        )
        print(df_sample)

        price = model.predict(df_sample)[0]
        price = round(price * 1000, 2)

        return html.Div([
            html.H4(f'Sugerowana cena {price}')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
