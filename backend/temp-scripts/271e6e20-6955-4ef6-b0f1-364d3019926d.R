library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/271e6e20-6955-4ef6-b0f1-364d3019926d.html')