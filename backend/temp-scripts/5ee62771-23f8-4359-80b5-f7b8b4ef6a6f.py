# Importing libraries
import numpy as np
from matplotlib import pyplot as plt

# Creating equally spaced 100 data in range 0 to 2*pi
theta = np.linspace(0, 1.5 * np.pi, 100)

# Generating x and y data
x = 16 * (np.sin(theta) ** 3)
y = 12 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)

# Plotting
plt.plot(x, y)
plt.title('Baburao')

plt.savefig('results/5ee62771-23f8-4359-80b5-f7b8b4ef6a6f.png')