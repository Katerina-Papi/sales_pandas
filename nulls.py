import pandas as pd

sales_df = pd.read_csv('Sales.csv')

find_nulls = sales_df.isnull() # searches for null values in df

sum_nulls = find_nulls.sum().sum() # sum of total nulls

print(sum_nulls)

#sales_df.to_csv('nulls.csv')

sales_df2 = sales_df.fillna('Unknown') # giving null values value of 'Unknown' in new df

find_nulls2 = sales_df2.isnull() # checks new df for null values
sum_nulls2 = find_nulls2.sum().sum() # checks sum of null values to see if any left
print(sum_nulls2)

sales_df2.to_csv('filled_nulls.csv') # write new df to csv to check results
