import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(
        id='tabs-1',
        children=[
            dcc.Tab(label='Python', value='py',),
            dcc.Tab(label='SQL', value='sql')
        ],
        value='py'
    ),

    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)

def render_content(tab):
    if tab == 'py':
        return html.Div([
            dcc.Markdown("""
            ```
            print('Hello Python')
            ```
            """)
        ])
    elif tab == 'sql':
        return html.Div([
            dcc.Markdown("""
            ```
            SELECT * FROM Customer;
            ```
            """)
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
