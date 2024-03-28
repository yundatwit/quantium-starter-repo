import pandas as pd

sales_one = pd.read_csv('daily_sales_data_0.csv')
sales_two = pd.read_csv('daily_sales_data_1.csv')
sales_three = pd.read_csv('daily_sales_data_2.csv')

sales_one = sales_one[sales_one['product'] == 'pink morsel']
sales_two = sales_two[sales_two['product'] == 'pink morsel']
sales_three = sales_three[sales_three['product'] == 'pink morsel']

sales_one['sales'] = sales_one['quantity'] * sales_one['price']
sales_two['sales'] = sales_two['quantity'] * sales_two['price']
sales_three['sales'] = sales_three['quantity'] * sales_three['price']

sales_one = sales_one[['product', 'date', 'region', 'sales']]
sales_two = sales_two[['product', 'date', 'region', 'sales']]
sales_three = sales_three[['product', 'date', 'region', 'sales']]

merged_sales = pd.concat([sales_one, sales_two, sales_three])

merged_sales = merged_sales.dropna()

merged_sales.to_csv('output.csv', index=False)