# Importing libraries
import numpy as np
from matplotlib import pyplot as plt

# Creating equally spaced 100 data in range 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Generating x and y datahttp://127.0.0.1:5000/results/2aa9fccf-ef88-4b08-b4e7-8b738b27b0e3.png
x = 12 * (np.sin(theta) ** 3)
y = 12 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)

# Plotting
plt.plot(x, y)
plt.title('Baburao')

plt.savefig('results/9c3b87f5-9048-466a-a339-a54da81e8df3.png')