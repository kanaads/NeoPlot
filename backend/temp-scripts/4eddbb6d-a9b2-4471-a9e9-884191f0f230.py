import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/neo-3ead7698-dee2-4909-b4ba-47bf1e4fbd1d.html')
plt.savefig('results/4eddbb6d-a9b2-4471-a9e9-884191f0f230.png')