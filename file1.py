import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FD8FF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Dash",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
    Dash: A web application framework for Python.
    ''',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),

    dcc.Graph(
        id='my-first-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [4, 5, 2], 'type': 'bar', 'name': u'Montréal'},
                {'x': [1, 2, 3], 'y': [6, 3, 2], 'type': 'bar', 'name': 'BK'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
