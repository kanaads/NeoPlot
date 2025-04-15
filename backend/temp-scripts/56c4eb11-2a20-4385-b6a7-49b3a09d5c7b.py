import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/56c4eb11-2a20-4385-b6a7-49b3a09d5c7b.html')
plt.savefig('results/56c4eb11-2a20-4385-b6a7-49b3a09d5c7b.png')