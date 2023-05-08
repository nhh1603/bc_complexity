# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter

# test = [0,1,2,2,3,3]
# block = []
# for i in range(len(test)-1):
#     block.append(test[i+1] - test[i])

# fig, axs = plt.subplots(1, 1, tight_layout=True)
# axs.hist(test, bins=3)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Generate some random data that follows a Poisson distribution
data = [0,1,1,2,2,3,4,5]

# Create a range of x values
x = np.arange(0, max(data) + 1)

# Compute the Poisson PMF
pmf = poisson.pmf(x, mu=np.mean(data))

# Plot the histogram of the data
plt.hist(data, bins=[0,1,2,3,4,5], density=True, alpha=0.5, label='Data')

# Plot the Poisson PMF
plt.plot(x, pmf, 'r', label='Poisson PMF')

# Add labels and a title
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Poisson Distribution')

# Add a legend
plt.legend()

# Show the plot
plt.show()