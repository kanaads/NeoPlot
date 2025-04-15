import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/7f8e0038-826b-45ec-a7e3-32b5f2515628.html')
plt.savefig('results/7f8e0038-826b-45ec-a7e3-32b5f2515628.png')