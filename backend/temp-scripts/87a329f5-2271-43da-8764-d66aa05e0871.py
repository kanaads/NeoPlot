import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/87a329f5-2271-43da-8764-d66aa05e0871.html')
plt.savefig('results/87a329f5-2271-43da-8764-d66aa05e0871.png')