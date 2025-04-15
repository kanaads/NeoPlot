import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-da37bb46-a1d7-4cde-886b-0116d4ee1b73.html')