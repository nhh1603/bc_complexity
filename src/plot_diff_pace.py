from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from tools import db, get_difficulty, get_time, average_block_paces_epoch

### Constants ###

measure_range = [350, 391]
difficulties = []
for i in range(measure_range[0], measure_range[1]):
    difficulty = get_difficulty(i * 2016)
    difficulties.append(difficulty)

average_block_paces = []
for i in range(measure_range[0], measure_range[1]):
    average = average_block_paces_epoch(i)
    average_block_paces.append(average)

difficulty_curr = get_difficulty(measure_range[0] * 2016)
difficulties_theoretical = [difficulty_curr]
for i in range(measure_range[0] + 1, measure_range[1]):
    difficulty_curr = difficulty_curr * (20160.0*60 / (get_time(i * 2016 - 1) - get_time((i - 1) * 2016)))
    difficulties_theoretical.append(difficulty_curr)


### Plotting ###
# x_axis = np.arange(370, 391, 1)
x_axis = [i for i in range(measure_range[0], measure_range[1], 1)]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Difficulty', color=color)
ax1.plot(x_axis, difficulties, color=color, label='Difficulties')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0, 5e13])

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Time (minutes)', color=color)  # we already handled the x-label with ax1
ax2.plot(x_axis, average_block_paces, color=color, label='Block Paces')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([5, 15])
plt.axhline(10, color='purple', linestyle='--', label='Average')

ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:green'
# ax3.set_ylabel('Theoretical Difficulty', color=color)  # we already handled the x-label with ax1
ax3.plot(x_axis, difficulties_theoretical, color=color, label='Theoretical Difficulties')
ax3.tick_params(axis='y', labelcolor=color)
ax3.set_ylim([0, 5e13])

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines = lines1 + lines2 + lines3
labels = labels1 + labels2 + labels3
plt.legend(lines, labels, loc='best')

plt.title("Difficulty & Block Pace Comparison")
fig.tight_layout()  # otherwise the right y-label is slightly clipped
fig.savefig('./results/Difficulty & Block Pace Comparison.png')

plt.show()