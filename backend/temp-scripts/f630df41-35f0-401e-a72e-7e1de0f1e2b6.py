import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/f630df41-35f0-401e-a72e-7e1de0f1e2b6.html')
plt.savefig('results/f630df41-35f0-401e-a72e-7e1de0f1e2b6.png')