import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-715f8fd9-3cd5-4b7d-9875-ef43d305b2bd.html')