import pandas as pd

def top_customer_by_profit(df, target_date):

    # Convert 'transaction date' column from "DD.MM.YYYY" to "YYYY-MM-DD"
    df['TransDate'] = pd.to_datetime(df['TransDate'], format='%d.%m.%Y')
    df.TransDate.apply(lambda x: x.strftime('%Y-%m-%d')).astype(str)

    # Calculate Profit = Purchase Amount - Cost
    df['Profit'] = df['PurchAmount'] - df['Cost']

    # Filter transactions for the given date
    daily_transactions = df[df['TransDate'] == target_date]

    # Group by customer and sum profits
    customer_profits = daily_transactions.groupby('Customer')['Profit'].sum()

    # Find the customer with the highest profit
    top_customer = customer_profits.idxmax()

    return top_customer

