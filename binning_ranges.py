import pandas as pd

# Read the data from a CSV file
data = pd.read_csv('max_ranges.csv', header=None, names=['Weekly_Range'], dtype={'Weekly_Range': float})

# Define the bins
bins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

# Use pd.cut to create bins
bin_labels = [f"{b}-{b+99}" for b in bins[:-1]]
data['Binned_Weekly_Range'] = pd.cut(data['Weekly_Range'], bins=bins, labels=bin_labels, right=False)

print(data)
data.to_csv('agg_bin_results.csv')


