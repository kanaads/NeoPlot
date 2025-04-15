library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/b80ea1a1-8230-4d8a-bb09-78c30ea35c34.html')