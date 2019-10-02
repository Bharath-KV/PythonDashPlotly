import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_style_sheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_style_sheets)

app.layout = html.Div([
    dcc.Input(id='my-input', value='Initial Value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_div(inp_val):
    return 'You\'ve entered {}'.format(inp_val)


if __name__ == '__main__':
    app.run_server(debug=True)
