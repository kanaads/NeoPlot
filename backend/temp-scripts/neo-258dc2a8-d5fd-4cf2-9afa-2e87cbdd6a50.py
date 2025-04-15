import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-258dc2a8-d5fd-4cf2-9afa-2e87cbdd6a50.html')