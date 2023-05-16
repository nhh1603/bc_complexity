import requests
import matplotlib.pyplot as plt
import pandas as pd

# Retrieve hash rate data

# Define the hash rate API endpoint
hash_rate_api_url = 'https://api.blockchain.info/charts/hash-rate'

# Set the parameters for the hash rate API request
hash_rate_params = {
    'timespan': '12years',  # Specify the desired time range
    'format': 'json'        # Specify the response format
}

# Send a GET request to the hash rate API endpoint
hash_rate_response = requests.get(hash_rate_api_url, params=hash_rate_params)

# Parse the JSON response for hash rate data
hash_rate_data = hash_rate_response.json()
hash_rate_values = [point['y'] for point in hash_rate_data['values']]
dates = pd.to_datetime([pd.Timestamp(point['x'], unit='s').date() for point in hash_rate_data['values']])

# Create a DataFrame for hash rate data
hash_rate_df = pd.DataFrame({'Hash Rate': hash_rate_values}, index=dates)

# Retrieve price data

# Define the price API endpoint
price_api_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

# Set the parameters for the price API request
price_params = {
    'start': '2011-05-15',
    'end': '2023-05-15'
}

# Send a GET request to the price API endpoint
price_response = requests.get(price_api_url, params=price_params)

# Parse the JSON response for price data
price_data = price_response.json()['bpi']
price_df = pd.DataFrame.from_dict(price_data, orient='index', columns=['Price'])
price_df.index = pd.to_datetime(price_df.index)

# Plotting both hash rate and price in the same figure

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot hash rate on the left y-axis
ax.plot(hash_rate_df.index, hash_rate_df['Hash Rate'], color='blue')
ax.set_ylabel('Hash Rate (EH/s)', color='blue')
ax.set_yscale('log')
ax.set_ylim([10**-2, 10**9])

# Create a twin y-axis for price
ax2 = ax.twinx()

# Plot price on the right y-axis
ax2.plot(price_df.index, price_df['Price'], color='green')
ax2.set_ylabel('Price (USD)', color='green')
ax2.set_yscale('log')
ax2.set_ylim([10**0, 10**11])


# Set the title and labels
ax.set_title('Bitcoin Hash Rate and Price Evolution')
ax.set_xlabel('Date')

plt.grid(axis='y')
# Show the plot
plt.show()
