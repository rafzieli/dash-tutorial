import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Notowania Amazon'),

    html.Table([
        html.Tr([
            html.Th('Date'),
            html.Th('Open'),
            html.Th('High'),
            html.Th('Low'),
            html.Th('Close'),
            html.Th('Volume')
        ]),

        html.Tr([
            html.Td('2019-09-01'),
            html.Td('100'),
            html.Td('102'),
            html.Td('98'),
            html.Td('101'),
            html.Td('15000')
        ]),

        html.Tr([
            html.Td('2019-09-02'),
            html.Td('101'),
            html.Td('103'),
            html.Td('79'),
            html.Td('87'),
            html.Td('14000')
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
