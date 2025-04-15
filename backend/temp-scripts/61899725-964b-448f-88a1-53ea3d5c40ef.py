import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/61899725-964b-448f-88a1-53ea3d5c40ef.html')
plt.savefig('results/61899725-964b-448f-88a1-53ea3d5c40ef.png')