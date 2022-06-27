import acquire
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sales_date_index(df):
    # Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    # Set the index as that date and then sort index (by the date)
    df = df.set_index("sale_date").sort_index()
    return df

def amount_price_plot(df):
    # Plot of the distribution of sale_amount to item_price
    sns.scatterplot(data = df, x = 'sale_amount', y = 'item_price')

def sales_new_columns(df):
    # Add a 'month' and 'day of week' column to your dataframe.
    df['month'] = df.index.strftime('%m') + ' ' + df.index.strftime('%b')
    df['day_of_week'] = df.index.strftime('%w') + ' ' + df.index.strftime('%a')
    # Add a column to your dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def pow_sys_index(df):
    #Convert date column to datetime format.
    df.Date = pd.to_datetime(df.Date, format = '%Y-%m-%d')
    # Set the index to be the datetime variable. (I will also sort)
    df = df.set_index('Date').sort_index()
    return df

def pow_sys_dist_plot(df):
    # Plot the distribution of each of your variables.
    for column in df.columns:
        sns.displot(data = df, x=column)

def pow_sys_new_col(df):
    # Add a month and a year column to your dataframe.
    df['month'] = df.index.strftime('%m') + ' ' + df.index.strftime('%b')
    df['year'] = df.index.strftime('%Y')

def pow_sys_fill_vals(df):
    df = df.fillna(0)
    return df