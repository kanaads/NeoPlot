library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/56699365-fadd-45c5-9de8-3ac93b61eab4.html')