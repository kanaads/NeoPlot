import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-9335bd52-8dcd-4e0c-baa6-e107108409d9.html')