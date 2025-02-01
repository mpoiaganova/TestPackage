import pandas as pd
from package.module import top_customer_by_profit

# Load the dataset
data_path = 'data/transactions.csv'
df = pd.read_csv(data_path)

# Run the function with the specified date
date_input = "2012-05-03"
best_profit = top_customer_by_profit(df, date_input)

# Print the result
print(f"Best customer for {date_input}:")
print(best_profit)
