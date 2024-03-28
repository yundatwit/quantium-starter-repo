import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

data = pd.read_csv('output.csv')
data['date'] = pd.to_datetime(data['date'])
data['sales'] = data['sales'].astype(float)
data = data.sort_values(by='date')

sales_before = data[data['date'] < '2021-01-15']['sales'].sum()
sales_after = data[data['date'] >= '2021-01-15']['sales'].sum()
difference = (sales_after - sales_before)

app = dash.Dash('Quantium')

app.layout = html.Div([
    html.H1("Visualization of Sales"),
    dcc.Graph(
        id = 'sales',
        figure = px.line(data, x = 'date', y = 'sales', title = 'Sales Over Time')
    ),
    html.Div([
        html.H3("Sales before January 15, 2021: ${:,.2f}".format(sales_before)),
        html.H3("Sales after January 15, 2021: ${:,.2f}".format(sales_after)),
        html.H3("Difference in sales: ${:,.2f}".format(difference))
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
