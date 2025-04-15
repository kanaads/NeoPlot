library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/a6d66c89-e1b1-4420-ae0e-0f552fbfe741.html')
plt.savefig('results/a6d66c89-e1b1-4420-ae0e-0f552fbfe741.png')