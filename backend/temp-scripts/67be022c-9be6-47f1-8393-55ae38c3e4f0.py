import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/67be022c-9be6-47f1-8393-55ae38c3e4f0.html')
plt.savefig('results/67be022c-9be6-47f1-8393-55ae38c3e4f0.png')