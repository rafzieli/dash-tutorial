import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

colors = {
    'background': '#68ed8c',
    'text':  '#6b756e'
}

app.layout = html.Div([

    html.H2('Hello Dash',
            style={
                'color': colors['text'],
                'textAlign': 'center'
            }),

    html.Div('Dash: A web application framework for Python.',
             style={
                 'color': colors['text'],
                 'textAlign': 'center'
             }),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[120, 154, 168],
                marker_color='#95b4ed',
                marker_line_color='#6b756e',
                marker_line_width=5,
                name='local'
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[160, 198, 268],
                marker_color='#061f4f',
                marker_line_color='#6b756e',
                marker_line_width=5,
                name='online'
            )
        ],
        layout=go.Layout(
            title='Wizualizacja danych',
            plot_bgcolor='#517a2f',
            paper_bgcolor=colors['background']
        )
        )
    )
], style={'backgroundColor': '#d1f2b6'})

if __name__ == '__main__':
    app.run_server(debug=True)
