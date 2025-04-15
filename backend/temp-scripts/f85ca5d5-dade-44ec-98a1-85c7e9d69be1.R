library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/f85ca5d5-dade-44ec-98a1-85c7e9d69be1.html')