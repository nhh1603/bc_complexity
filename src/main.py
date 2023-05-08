import requests
import bitcoin_explorer as bex
from datetime import datetime

# bitcoin_api = 'https://api.blockchair.com/bitcoin/blocks'
# # # Make a request to the Blockchair API to retrieve the Bitcoin ledger
# # response = requests.get('https://api.blockchair.com/bitcoin/blocks')

# # Get the current Bitcoin block difficulty from a blockchain API, e.g. blockchain.info
# response = requests.get('https://blockchain.info/q/getdifficulty')
# current_difficulty = int(float(response.text)) + 1

# print(current_difficulty)
# # Make a request to the Blockchair API to retrieve the last block with the same difficulty
# response = requests.get(f'https://api.blockchair.com/bitcoin/blocks?q=difficulty({current_difficulty})')

# # Parse the response as JSON
# json_data = response.json()
# print(json_data)
# # Print the block hash and height of the first block in the ledger
# first_block = json_data['data'][0]
# print('Block hash:', first_block['hash'])
# print('Block time:', first_block['time'])
# print('Block difficulty:', first_block['difficulty'])
# second_block = json_data['data'][1]
# time1 = datetime.strptime(first_block['time'], '%Y-%m-%d %H:%M:%S')
# time2 = datetime.strptime(second_block['time'], '%Y-%m-%d %H:%M:%S')
# print(time1)
# # Calculate the time difference as a timedelta object
# time_diff = time1 - time2

# # Print the time difference in seconds
# print('Time difference:', time_diff.seconds, 'seconds')

db = bex.BitcoinDB("D:/Coding/Bitcoin/Data", False)
count = db.get_max_height()
print(count)
# time = datetime.fromtimestamp(count).strftime("%A, %B %d, %Y %I:%M:%S")
# print(time)
