import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def get_best_profit(df, date):
    # Filter data for the given date
    df_filtered = df[df['TransDate'] == date]
    
    # Calculate profit per customer
    df_filtered['Profit'] = df_filtered['PurchAmount'] - df_filtered['Cost']
    
    # Group by customer and sum profits
    result = df_filtered.groupby('Customer')['Profit'].sum().reset_index()
    
    # Find the customer with the maximum profit
    max_profit_customer = result[result['Profit'] == result['Profit'].max()]
    
    # Return the result
    return max_profit_customer[['Customer', 'Profit']]

# Set the working directory (adapt this path to your project structure)
os.chdir('/path/to/your/project/directory')

# Load the data
data = load_data('data/transactions.csv')

# Get the best profit for a specific date
best_profit = get_best_profit(data, '2006-01-31')
print(best_profit)
