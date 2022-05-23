import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def fetch_financial_data(company='AMZN'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df = df.reset_index()
df = df[:20]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    columns=[{'name': col, 'id': col} for col in df.columns],
    data=df.to_dict('records')
)

if __name__ == '__main__':
    app.run_server(debug=True)
