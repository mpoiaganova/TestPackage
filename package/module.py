import pandas as pd

def get_best_profit(df, date):
    # Keep TransDate as strings in the format 'dd.mm.yyyy'

    # Calculate profit per customer
    df['Profit_Customer'] = df['PurchAmount'] - df['Cost']

    # Aggregate profit per customer where TransDate equals the given date
    profit_per_customer = df[df['TransDate'] == date].groupby('Customer')['Profit_Customer'].sum().reset_index()

    # Find the customer with the maximum profit for that date
    if not profit_per_customer.empty:
        max_profit = profit_per_customer['Profit_Customer'].max()
        best_customer = profit_per_customer[profit_per_customer['Profit_Customer'] == max_profit]['Customer'].iloc[0]

        # Convert numpy types to Python native types
        return {
            'Date': date,
            'Best Customer': int(best_customer),
            'Best Profit': float(max_profit)
        }
    else:
        return {'Date': date, 'Message': 'No transactions found for this date'}


# Example usage:
df = pd.read_csv('../data/transactions.csv')
result = get_best_profit(df, '18.10.2005')
print(result)

