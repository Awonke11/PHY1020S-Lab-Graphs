from matplotlib import pyplot as plt
import numpy as np
from parallelPlates import parallel_x_values, parallel_y_values
from insulator import insulator_x_values, insulator_y_values
from circularPlate import circular_x_values, circular_y_values

# [X, Y] = np.meshgrid(parallel_x_values, parallel_y_values)

fig, ax = plt.subplots(2, 2)
fig.set_figheight(6)
fig.set_figwidth(12)
fig.subplots_adjust(hspace=0.5, wspace=0.2)

ax[0, 0].set_title("Two parallel plates")
ax[0, 0].set_xlabel("x-coordinates")
ax[0, 0].set_ylabel("y-coordinates")
ax[0, 0].scatter(parallel_x_values, parallel_y_values)

ax[0, 1].set_title("Parallel Plates with insulator")
ax[0, 1].set_xlabel("x-coordinates")
ax[0, 1].set_ylabel("y-coordinates")
ax[0, 1].scatter(insulator_x_values, insulator_y_values)

ax[1, 0].set_title("One plate and one circular ring")
ax[1, 0].set_xlabel("x-coordinates")
ax[1, 0].set_ylabel("y-coordinates")
ax[1, 0].scatter(circular_x_values, circular_y_values)

plt.show()
