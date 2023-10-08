import pandas as pd

# Read the data from a CSV file
data = pd.read_csv('max_ranges.csv', header=None, names=['Weekly_Range'], dtype={'Weekly_Range': float})

# Define the bins
bins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

# Use pd.cut to create bins
bin_labels = [f"{b}-{b+99}" for b in bins[:-1]]
data['Binned_Weekly_Range'] = pd.cut(data['Weekly_Range'], bins=bins, labels=bin_labels, right=False)

# Group by the binned column and calculate the count
agg_data = data.groupby('Binned_Weekly_Range').agg({'Weekly_Range': 'count'}).reset_index()

# Rename the columns for clarity
agg_data.rename(columns={'Weekly_Range': 'Count'}, inplace=True)

# Calculate the percentage column
agg_data['Percentage'] = (agg_data['Count'] / agg_data['Count'].sum()) * 100

print(data)
data.to_csv('bin_results.csv')

print(agg_data)
agg_data.to_csv('agg_data.csv')

