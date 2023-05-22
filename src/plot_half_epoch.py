import matplotlib.pyplot as plt

from tools import get_block_pace

### Constants ###
# epoch = 60
# block_paces = get_block_pace(epoch)
# average1 = sum(block_paces[:len(block_paces)//2])
# average2 = sum(block_paces[len(block_paces)//2:])
x_axis = [i*2 for i in range(195)]
first_half = []
second_half = []
for i in range(195):
    # block_paces = []
    block_paces = get_block_pace(i*2)
    first_half.append(sum(block_paces[:len(block_paces)//2]))
    second_half.append(sum(block_paces[len(block_paces)//2:]))

### Plotting ###

fig, ax = plt.subplots()

# Plot the first set of data
ax.plot(x_axis, first_half, label='First half of epoch', color='b')

# Plot the second set of data
ax.plot(x_axis, second_half, label='Second half of epoch', color='r')

# Set the title and axis labels
plt.title('Time taken to mine in first and second half of epoch')
plt.xlabel('Epoch')
plt.ylabel('TIme (seconds)')
plt.grid(axis='y')
plt.legend()
# Show the plot
plt.show()