import pandas as pd

# Example data
data = {
    'TransDate': ['2023-01-15', '2023-01-20', '2023-02-10'],
    'PurchAmount': [120, 150, 130],
    'Cost': [50, 70, 60],
    'Customer': ['A', 'B', 'A']
}
x = pd.DataFrame(data)

# Convert dates ensuring no errors and dropping NaT values before applying tz_localize
x['TransDate'] = pd.to_datetime(x['TransDate'], errors='coerce')
x.dropna(subset=['TransDate'], inplace=True)  # Drop any rows that resulted in NaT

# Now apply timezone localization
x['TransDate'] = x['TransDate'].dt.tz_localize('UTC')

print(x['TransDate'].head())
