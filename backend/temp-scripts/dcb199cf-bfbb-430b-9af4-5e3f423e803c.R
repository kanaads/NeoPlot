library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/dcb199cf-bfbb-430b-9af4-5e3f423e803c.html')