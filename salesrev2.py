import pandas as pd

df = pd.read_csv('Sales.csv')

profit_per_state_year = df.groupby(['State', 'Year'])['Profit'].sum().reset_index() # sum of profits per state and year
#print(profit_per_state_year)

profit_per_state_year.to_csv('salesrev2.csv') # reading state, year and profit sums to csv for checks

profit_per_state_year['Profit_Change'] = profit_per_state_year.groupby('State')['Profit'].diff() # difference in profits now called profit change
# only groupby state not state and year to get diff of consecutive rows for each state across all years  
profit_per_state_year.to_csv('salesrev2.1.csv') # writing to csv to check profit diff

profit_per_state_year['Percentage_Change'] = profit_per_state_year.groupby('State')['Profit'].pct_change() * 100 # calculates percentage change of profit each year per state 
profit_per_state_year['Percentage_Change'] = profit_per_state_year['Percentage_Change'].round(2)
profit_per_state_year.to_csv('salesrev2.2.csv') # writing to csv to check pct change to 2 dp

# locates 'profit change' in df, then uses idxmax to locate index of row with highest number in 'profit change'
# loc is used to access the row corresponding with the idxmax 
# will return as a series
largest_profit_increase = profit_per_state_year.loc[profit_per_state_year['Profit_Change'].idxmax()]

print(largest_profit_increase)

# state = largest_profit_increase['State']
# year = largest_profit_increase['Year']
# profit_change = largest_profit_increase['Profit_Change']
# percentage_change = profit_per_state_year['Percentage_Change']

# print(state, year, profit_change, percentage_change)