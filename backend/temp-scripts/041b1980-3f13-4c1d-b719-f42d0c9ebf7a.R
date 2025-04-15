library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/041b1980-3f13-4c1d-b719-f42d0c9ebf7a.html')