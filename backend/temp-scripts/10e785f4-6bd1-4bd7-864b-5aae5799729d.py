import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/10e785f4-6bd1-4bd7-864b-5aae5799729d.html')
plt.savefig('results/10e785f4-6bd1-4bd7-864b-5aae5799729d.png')