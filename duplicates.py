import pandas as pd

sales_df = pd.read_csv('Sales.csv')

#sales_df['Duplicate'] = sales_df.duplicated() # finds dupes and creates to col called Duplicate 

sales_df.drop_duplicates(inplace=True)

dupicates = sales_df.duplicated()

num_duplicates = dupicates.sum()
print(num_duplicates)

sales_df.to_csv('dropped_dupes.csv', index=False)

#sales_df.to_csv('dropped_dupes.csv')

# sales_df_sorted_dupes = sales_df.sort_values(by=['Duplicate'], ascending=False) # sort df by duplicate col starting with True values

# drop_dupes = sales_df.drop_duplicates()
# sum_drop_dupes = drop_dupes.duplicated().sum()
# print(drop_dupes)
# print(sum_drop_dupes)

# drop_dupes.to_csv('dropped_dupes.csv')

#sales_df_duplicates = sales_df['Date', 'State'].duplicated() # to compare selected cols

# sales_df = sales_df.duplicated() # finds duplicates based on all cols
# print(sales_df)

# sum_sales_df_duplicates = sales_df.duplicated().sum() # finds the sum of duplicates 
# print(sum_sales_df_duplicates) 
