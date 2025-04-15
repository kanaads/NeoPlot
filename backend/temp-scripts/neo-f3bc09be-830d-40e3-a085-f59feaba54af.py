import os
os.makedirs('results', exist_ok=True)
import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-f3bc09be-830d-40e3-a085-f59feaba54af.html')