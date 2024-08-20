import pandas as pd

sales_df = pd.read_csv('Sales.csv')

sales_df['Date'] = pd.to_datetime(sales_df['Date'], errors='coerce') 
# convert the date col to datetime whilst ensuring invalid dates are converted to NaT

#print(sales_df.head())

print(sales_df)

print(sales_df.isnull().sum()) # show amount of missing values to check it worked in date col

sales_df = sales_df.fillna('Invalid') # replace all missing values to Invalid

print(sales_df)

sales_df_new_dates = sales_df.to_csv('newdates.csv')