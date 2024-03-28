import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

data = pd.read_csv('output.csv')
data['date'] = pd.to_datetime(data['date'])
data['sales'] = data['sales'].astype(float)
data = data.sort_values(by='date')

regions = ['north', 'east', 'south', 'west', 'all']

app = dash.Dash('Quantium')

app.layout = html.Div([
    html.H1("Visualization of Sales"),
    dcc.RadioItems(
        id = 'Select-Region',
        options=[{'label': region.capitalize(), 'value': region} for region in regions],
        value='all',
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(
        id='sales'
    )
    ])

def update_chart(selection_of_region):
    if selection_of_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == selection_of_region]

    fig = px.line(filtered_data, x = 'date', y = 'sales', title = 'Sales Over Time')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
