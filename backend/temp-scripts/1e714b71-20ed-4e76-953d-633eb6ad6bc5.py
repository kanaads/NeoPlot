library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/1e714b71-20ed-4e76-953d-633eb6ad6bc5.html')