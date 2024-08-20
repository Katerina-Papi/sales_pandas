import pandas as pd

sales_data = pd.read_csv('Sales.csv')

# VERIFYING CALCULATIONS BY CHECKING VAL D'OISE SUM IN 2013
# val_profit = sales_data.loc[(sales_data['Year'] == 2013) & (sales_data['State'] == "Val d'Oise"), 'Profit'].sum()
# print(val_profit)

# sales_data.sort_values(by=['State', 'Year'], inplace=True)

# Calculate the total profit per state and year
profit_per_state_year = sales_data.groupby(['State', 'Year'])['Profit'].sum().reset_index()
#profit_per_state_year.to_csv('salesrev1.csv')

# Calculate the year-to-year change in profit for each state
profit_per_state_year['Profit_Change'] = profit_per_state_year.groupby('State')['Profit'].diff()
profit_per_state_year['Percentage_Change'] = profit_per_state_year.groupby('State')['Profit'].pct_change() * 100
profit_per_state_year['Percentage_Change'] = profit_per_state_year['Percentage_Change'].round(2)
profit_per_state_year = profit_per_state_year.sort_values(by=['Percentage_Change'], ascending=False)
print(profit_per_state_year)
profit_per_state_year.to_csv('salesrev1.1.csv')

# Find the state with the largest increase in profit
max_profit_increase = profit_per_state_year.loc[profit_per_state_year['Percentage_Change'].idxmax()]

# Extract the details
state = max_profit_increase['State']
year = max_profit_increase['Year']
percentage_change = max_profit_increase['Percentage_Change']

print(state, year, percentage_change)
