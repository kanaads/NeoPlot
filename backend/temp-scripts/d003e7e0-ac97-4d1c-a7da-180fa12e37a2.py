import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('results/d003e7e0-ac97-4d1c-a7da-180fa12e37a2.html')
plt.savefig('results/d003e7e0-ac97-4d1c-a7da-180fa12e37a2.png')