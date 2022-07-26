#This script takes in the tempe traffic data and performs basic ETL to output a clean data file
#dependent on pandas and python 3.9 +
import pandas as pd

initial_data = pd.read_csv("/users/n/Tempe_Traffic_V.2/traffic_data.2.csv")

#checking data for null values
initial_data.isnull().sum()

#3537 missing values / incomplete records
num_missing_values = initial_data.isnull().sum().max()

#around 8.9% of the values were taken out of the dataset, alternate methods for na values will be explored in other files
percent_missing = num_missing_values / (len(initial_data))

no_null_vals_df = initial_data.dropna()
null_vals_df = initial_data

no_null_vals_df

#fixing datetime
no_null_vals_df["DateTime"] = no_null_vals_df["DateTime"].astype('datetime64[ns]')
null_vals_df["DateTime"] = null_vals_df["DateTime"].astype('datetime64[ns]')


#saving new files
no_null_vals_df.to_csv("no_null_vals_df.csv", index=False)
null_vals_df.to_csv("null_vals_df.csv", index = False)
