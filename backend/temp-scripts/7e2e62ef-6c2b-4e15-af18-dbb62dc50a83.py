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
fig.write_html('results/7e2e62ef-6c2b-4e15-af18-dbb62dc50a83.html')
