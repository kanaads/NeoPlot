import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/c5b2b177-da0e-4c6b-a72c-c6ba093e7fb8.html')
plt.savefig('results/c5b2b177-da0e-4c6b-a72c-c6ba093e7fb8.png')