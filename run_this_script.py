import os
import pandas as pd
from package.module import get_best_profit  # Import the function

# OPTIONAL: Set the working directory if needed
# os.chdir('/path/to/your/project/directory')

# Load the dataset
data_path = 'data/transactions.csv'
df = pd.read_csv(data_path)

# Run the function with the specified date
date_input = "2006-01-31"
best_profit = get_best_profit(df, date_input)

# Print the result
print(f"Best customer for {date_input}:")
print(best_profit)
