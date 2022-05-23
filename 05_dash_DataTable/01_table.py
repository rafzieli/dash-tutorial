import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    columns=[
        {'name': 'UserID', 'id': 'UserID'},
        {'name': 'Rating', 'id': 'Rating'},
        {'name': 'Age', 'id': 'Age'}
    ],
    data=[
        {'UserID': '001', 'Rating': '4.5', 'Age': '24'},
        {'UserID': '002', 'Rating': '3.5', 'Age': '25'},
        {'UserID': '003', 'Rating': '2.5', 'Age': '45'},
        {'UserID': '004', 'Rating': '4.2', 'Age': '34'}
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
