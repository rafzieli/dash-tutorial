import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.DatePickerSingle(
        date=dt(2022, 5, 11)
    ),

    dcc.DatePickerSingle(
        date=dt(2022, 5, 11),
        display_format='YYYY-MM-DD'
    ),

    dcc.DatePickerSingle(
        date=dt(2022, 5, 11),
        display_format='DD-MM-YYYY'
    ),

    dcc.DatePickerRange(
        start_date=dt(2020,9,1),
        end_date=dt(2020,10,31)
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
