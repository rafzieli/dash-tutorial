import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[219, 156, 453],
                    name='Sales USA',
                    marker=go.bar.Marker(
                        color='rgb(53, 83, 109)'
                    )
                ),
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[342, 324, 543],
                    name='Sales Europe',
                    marker=go.bar.Marker(
                        color='rgb(76, 23, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='Sales in Usa and Europe',
                showlegend=True
            )
        )
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
