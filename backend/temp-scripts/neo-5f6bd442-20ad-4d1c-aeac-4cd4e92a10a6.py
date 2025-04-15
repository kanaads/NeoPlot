import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-5f6bd442-20ad-4d1c-aeac-4cd4e92a10a6.html')