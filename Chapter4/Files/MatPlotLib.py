
# So you want to graph!

import matplotlib.pyplot as plt

# It begins easy enough, does the shown graph make sense?

plt.title('Some Data Graphed')
plt.plot([1, 2, 3, 4])
plt.ylabel('Numbers')
plt.show()

# How about with (x, y) pairs?

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# Categorical Data?, 3 in 1?

names = ['A', 'B', 'C']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.show()

# Pretty cool! You can find more in the MatPlotLib documentation, and some in the Pandas.py file!