import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
plt.draw()
plt.pause(5)