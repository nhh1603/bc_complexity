import matplotlib.pyplot as plt

from tools import get_block_pace

### Constants ###
epoch = 300
block_paces = get_block_pace(epoch)
average1 = sum(block_paces[:len(block_paces)//2])
average2 = sum(block_paces[len(block_paces)//2:])

### Plotting ###
# x_axis = np.arange(370, 391, 1)
x_axis = [epoch*2016+i for i in range(2015)]
plt.plot(x_axis, block_paces, color='r', label='diff')
plt.xlabel("Block index")
plt.ylabel("Time (minutes)")
# plt.yscale('log')
plt.title("Evolution of block paces in epoch 300")

plt.show()