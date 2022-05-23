import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H3('Hello World - porownanie'),

    dcc.Tabs(
        children=[
            dcc.Tab(
                label='Python',
                children=[
                    dcc.Markdown(
                        """
                        ```
                        print('Hello World')
                        ```
                        """
                    )
                ]
            ),
            dcc.Tab(
                label='Java',
                children=[
                    dcc.Markdown(
                        """
                        ```
                        class HelloWorld {
                            public static void main(String[] args) {
                                System.out.println("Hello, World!"); 
                            }
                        }
                        ```
                        """
                    )
                ]
            )
        ]
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
