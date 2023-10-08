import yfinance as yf
import pandas as pd
import plotly.express as px

# Define the stock symbol and date range
stock_symbol = "NQ=F"  # Change this to your desired stock symbol
start_date = "2011-01-01"
end_date = "2023-10-06"

# Fetch historical data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Create a DataFrame
df = pd.DataFrame(stock_data)

# Calculate the difference between rows
df['Price_Difference'] = df['Close'].diff()

# Add a column for the day of the week
df['Day_of_Week'] = df.index.dayofweek

# Resample data on a weekly basis (Monday to Sunday)
weekly_data = df.resample('W-MON').agg({'Low': 'min', 'High': 'max'})

# Calculate the difference between the lowest low and the highest high for each week
weekly_data['Weekly_Range'] = weekly_data['High'] - weekly_data['Low']

# Create a histogram using Plotly
fig = px.histogram(weekly_data, x="Weekly_Range", title="Frequency Distribution of Weekly Ranges")
fig.update_xaxes(title="Weekly Range")
fig.update_yaxes(title="Frequency")

# Calculate the frequency distribution
histogram_data = weekly_data['Weekly_Range'].value_counts().reset_index()
histogram_data.columns = ['Weekly_Range', 'Count']

# Print the resulting DataFrame
print(histogram_data)

# Save the histogram data to a CSV file
histogram_data.to_csv('frequency_distribution.csv', index=False)

# fig.write_html('NQ_range.html', auto_open=True)

data = histogram_data[['Weekly_Range']]

# Define the bins
bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

# Use pd.cut to create bins
bin_labels = [f"{b}-{b+99}" for b in bins[:-1]]
data['Binned_Weekly_Range'] = pd.cut(data['Weekly_Range'], bins=bins, labels=bin_labels, right=False)

print(data)
data.to_csv('bin_results.csv')

# Group by the binned column and calculate the count
agg_data = data.groupby('Binned_Weekly_Range').agg({'Weekly_Range': 'count'}, observed=True).reset_index()

# Rename the columns for clarity
agg_data.rename(columns={'Weekly_Range': 'Count'}, inplace=True)

# Calculate the percentage column
agg_data['Percentage'] = (agg_data['Count'] / agg_data['Count'].sum()) * 100

agg_data['Cumulative_Percentage'] = agg_data['Percentage'].cumsum()

# Calculate the inverse of the cumulative percentages
agg_data['Inverse_Cumulative_Percentage'] = 100 - agg_data['Cumulative_Percentage']

print(agg_data['Inverse_Cumulative_Percentage'])
agg_data.to_csv('agg_data.csv')

