import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from tools import db, get_difficulty, average_block_paces_epoch

### Constants ###
difficulties = []

for i in range(391):
    difficulty = get_difficulty(i * 2016)
    difficulties.append(difficulty)

average_block_paces = []
for i in range(391):
    average = average_block_paces_epoch(i)
    average_block_paces.append(average)


### Plotting ###
# x_axis = np.arange(370, 391, 1)
x_axis = [i for i in range(391)]
plt.plot(x_axis, difficulties, color='r', label='diff')
plt.xlabel("Epoch")
plt.ylabel("Difficulty (10^13)")
# plt.yscale('log')
plt.title("Evolution of difficulty")

plt.show()