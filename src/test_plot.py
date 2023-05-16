import requests
import matplotlib.pyplot as plt
import pandas as pd

# Define the API endpoint
api_url = 'https://api.blockchain.info/charts/hash-rate'

# Set the parameters for the API request
params = {
    'timespan': '12years',  # Specify the desired time range
    'format': 'json'        # Specify the response format
}

# Send a GET request to the API endpoint
response = requests.get(api_url, params=params)

# Parse the JSON response
data = response.json()

# Extract the hash rate values and dates from the response
hash_rate_values = [point['y'] for point in data['values']]
dates = pd.to_datetime([pd.Timestamp(point['x'], unit='s').date() for point in data['values']])

# Create a DataFrame using the extracted data
df = pd.DataFrame({'Hash Rate': hash_rate_values}, index=dates)

# Plot the hash rate evolution
df.plot(kind='line')

# Set the plot title and axis labels
plt.title('Bitcoin Network Hash Rate Evolution')
plt.xlabel('Date')
plt.ylabel('Hash Rate (EH/s)')
plt.yscale('log')
plt.grid(axis='y')

# Show the plot
plt.show()