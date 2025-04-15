import os
os.makedirs('results', exist_ok=True)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Sample Chart")
plt.savefig('results/neo-c459c48c-92a3-44ce-b794-994c95de2b6b.png')