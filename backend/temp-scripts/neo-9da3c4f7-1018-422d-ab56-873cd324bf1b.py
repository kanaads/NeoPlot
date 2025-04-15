import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-9da3c4f7-1018-422d-ab56-873cd324bf1b.html')