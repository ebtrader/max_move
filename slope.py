import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = "NQ=F"  # Change this to your desired stock symbol
start_date = "2020-01-01"
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

# Print the resulting DataFrame
print(weekly_data)

# # Print the resulting DataFrame
# print(df)

weekly_data.to_csv('max_move.csv')

