library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/8d5c70bc-4a2d-4a65-a5e3-ea64d99e8662.html')