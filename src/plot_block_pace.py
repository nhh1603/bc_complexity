import bitcoin_explorer as bex

from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

from tools import db

### Constants ###
bins_sequence = np.arange(0, 40, 2)
# Compute the Poisson PMF
pmf = poisson.pmf(bins_sequence, mu=10)


### Functions ###
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


### Plotting ###
fig, axs = plt.subplots(2, 2)
fig.suptitle('Block Pace Distribution', fontsize = 20)

block_paces = retrieve_block_paces_epoch(0)
axs[0, 0].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
axs[0, 0].plot(bins_sequence, pmf, 'r', label='Poisson PMF')
axs[0, 0].set_xlabel('Pace (minutes)')
axs[0, 0].set_ylabel('Probability')
axs[0, 0].set_title('Epoch 0')
axs[0, 0].legend()

block_paces = retrieve_block_paces_epoch(150)
axs[0, 1].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
axs[0, 1].plot(bins_sequence, pmf, 'r', label='Poisson PMF')
axs[0, 1].set_xlabel('Pace (minutes)')
axs[0, 1].set_ylabel('Probability')
axs[0, 1].set_title('Epoch 150')
axs[0, 1].legend()

block_paces = retrieve_block_paces_epoch(300)
axs[1, 0].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
axs[1, 0].plot(bins_sequence, pmf, 'r', label='Poisson PMF')
axs[1, 0].set_xlabel('Pace (minutes)')
axs[1, 0].set_ylabel('Probability')
axs[1, 0].set_title('Epoch 300')
axs[1, 0].legend()

block_paces = retrieve_block_paces_all()
axs[1, 1].hist(block_paces, bins=bins_sequence, density=True, alpha=0.7, label='Block Pace')
axs[1, 1].plot(bins_sequence, pmf, 'r', label='Poisson PMF')
axs[1, 1].set_xlabel('Pace (minutes)')
axs[1, 1].set_ylabel('Probability')
axs[1, 1].set_title('All Time')
axs[1, 1].legend()


fig.savefig('./results/Block pace distribution.png')  # Save the figure to file.
plt.show()

