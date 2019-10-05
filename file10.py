import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-state-one', type='text', value='BK'),
    dcc.Input(id='input-state-two', type='text', value='Software Developer'),
    html.Button(id='submit-button', n_clicks=0, children='SUBMIT'),
    html.Div(id='output-state')
])


@app.callback(
    Output('output-state', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-state-one', 'value'),
     State('input-state-two', 'value')]
)
def update_state(n_clicks, state_one, state_two):
    return '''The Submit Button has been pressed {} times.\n
              Hi my name is {}, and I'm a {}.
    '''.format(n_clicks, state_one, state_two)


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
