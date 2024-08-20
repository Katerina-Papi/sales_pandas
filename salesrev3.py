# THIS METHOD HAS MORE POTENTIAL FOR ERRORS AS IT'S WORKING ON THE ORIGINAL DATAFRAME SO ANY MISSING VALUES / DUPLICATES CAN CAUSE
# ISSUES WHEN CALCULATING  

import pandas as pd

df = pd.read_csv('Sales.csv')

df['Total_Profit'] = df.groupby(['State', 'Year'])['Profit'].transform('sum') # creating new col named 'Total_Profit' for sum of profits per year for each state
# CHECKING TOTALS BELOW
# select_cols = df[['State', 'Year', 'Total_Profit']]
# print(select_cols)
# df.to_csv('salesrev3.1.csv')

df.sort_values(by=['State', 'Year'], inplace=True) # sorting in order of state then year
df.to_csv('salesrev3.2.csv') # checking by writing to new csv

df['Profit_Diff'] = df.groupby(['State'])['Total_Profit'].transform('diff') 
# adding new col to df called Profit_Diff which calculates the diff between total profits for each state
df.to_csv('salesrev3.3.csv')

df['Percentage_Change'] = df.groupby(['State'])['Total_Profit'].pct_change()*100 
# calculates pct change between total profit for each state 
df['Percentage_Change'] = df['Percentage_Change'].round(2) # rounds pct change to 2 dp
df.to_csv('salesrev3.4.csv')

# largest_profit_increase = df.loc[df['Percentage_Change'].idxmax()]

# print(largest_profit_increase)
