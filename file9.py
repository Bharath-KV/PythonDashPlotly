import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'India': ['Bangalore', 'Delhi', 'Bombay'],
    'Japan': ['Hiroshima', 'Nagasaki', 'Tokyo']
}

app.layout = html.Div([
    dcc.RadioItems(
        id='country-group',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='India'
    ),
    html.Hr(),
    dcc.RadioItems(id='city-group'),
    html.Hr(),
    html.Div(id='display-selected-value')
])


@app.callback(
    Output('city-group', 'options'),
    [Input('country-group', 'value')]
)
def update_city_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('city-group', 'value'),
    [Input('city-group', 'options')]
)
def update_city_values(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-value', 'children'),
    [Input('country-group', 'value'),
     Input('city-group', 'value')]
)
def update_output(selected_country, selected_city):
    return '{} is a city in {}'.format(selected_city, selected_country)


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
