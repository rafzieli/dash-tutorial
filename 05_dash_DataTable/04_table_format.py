import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table import FormatTemplate
import pandas as pd
from collections import OrderedDict

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame(OrderedDict([
    ('country', ['Poland', 'USA', 'Germany']),
    ('gdp', [100, 200, 150]),
    ('change', [0.07, 0.05, 0.04])
]))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dash_table.DataTable(
        columns=[
            {'name': 'Country', 'id': 'country', 'type': 'text'},
            {'name': 'GDP', 'id': 'gdp', 'type': 'numeric', 'format': FormatTemplate.money(0)},
            {'name': 'Change', 'id': 'change', 'type': 'numeric', 'format': FormatTemplate.percentage(1)}
        ],
        data=df.to_dict('records')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
