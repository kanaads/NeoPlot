import os
os.makedirs('results', exist_ok=True)
import plotly.graph_objects as go
import numpy as np

# Sample 3D data
np.random.seed(0)
x, y, z = np.random.randn(3, 100)

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(size=5)
)])
fig.update_layout(title='Interactive 3D Scatter Plot')
# Write the interactive plot as an HTML file
fig.write_html('charts/neo-5f6bd442-20ad-4d1c-aeac-4cd4e92a10a6.html')