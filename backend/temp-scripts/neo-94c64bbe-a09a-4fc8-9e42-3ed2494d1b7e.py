import os
os.makedirs('results', exist_ok=True)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4,10, 10])

plt.savefig('results/neo-94c64bbe-a09a-4fc8-9e42-3ed2494d1b7e.png')