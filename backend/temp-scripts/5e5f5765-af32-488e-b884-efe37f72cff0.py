import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/5e5f5765-af32-488e-b884-efe37f72cff0.html')
plt.savefig('results/5e5f5765-af32-488e-b884-efe37f72cff0.png')