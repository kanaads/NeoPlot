library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/c1acd8b1-97eb-492d-93bf-2d46579a6e4d.html')