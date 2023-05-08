import bitcoin_explorer as bex

from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


global db 
data_path = "D:/Coding/Bitcoin/Data"
db = bex.BitcoinDB(data_path, False)
bins_sequence = [i for i in range(40)]

def retrieve_block_paces_epoch(difficulty_times):
    block_paces = []
    times = []

    for i in range(2016):
        height = difficulty_times * 2016 + i
        time = int(db.get_block_header(height)['block_header']['time'])
        times.append(time)

    for i in range(len(times) - 1):
        time1 = times[i+1]
        time2 = times[i]
        block_paces.append((time1 - time2)/60.0)

    return block_paces

def retrieve_block_paces_all():
    block_paces = []
    times = []

    current_height = db.get_max_height()
    for i in range(current_height):
        time = int(db.get_block_header(i)['block_header']['time'])
        times.append(time)

    for i in range(len(times) - 1):
        time1 = times[i+1]
        time2 = times[i]
        block_paces.append((time1 - time2)/60.0)

    return block_paces

# average = sum(block_paces) / len(block_paces)
# print(average)

fig, axs = plt.subplots(2, 2)

block_paces = retrieve_block_paces_epoch(0)
axs[0, 0].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
# plt.hist(block_paces, bins=bins_sequence, density=True, alpha=0.5, label='Data')
axs[0, 0].set_xlabel('Pace (minutes)')
axs[0, 0].set_ylabel('Probability')
axs[0, 0].set_title('Block pace distribution for epoch 0')
axs[0, 0].legend()

block_paces = retrieve_block_paces_epoch(100)
axs[0, 1].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
# plt.hist(block_paces, bins=bins_sequence, density=True, alpha=0.5, label='Data')
axs[0, 1].set_xlabel('Pace (minutes)')
axs[0, 1].set_ylabel('Probability')
axs[0, 1].set_title('Block pace distribution for epoch 100')
axs[0, 1].legend()

block_paces = retrieve_block_paces_epoch(200)
axs[1, 0].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
# plt.hist(block_paces, bins=bins_sequence, density=True, alpha=0.5, label='Data')
axs[1, 0].set_xlabel('Pace (minutes)')
axs[1, 0].set_ylabel('Probability')
axs[1, 0].set_title('Block pace distribution for epoch 200')
axs[1, 0].legend()

block_paces = retrieve_block_paces_all()
axs[1, 1].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
# plt.hist(block_paces, bins=bins_sequence, density=True, alpha=0.5, label='Data')
axs[1, 1].set_xlabel('Pace (minutes)')
axs[1, 1].set_ylabel('Probability')
axs[1, 1].set_title('Block pace distribution of all time')
axs[1, 1].legend()

fig.savefig('./results/Block pace distribution.png', dpi=200)  # Save the figure to file.

plt.show()

