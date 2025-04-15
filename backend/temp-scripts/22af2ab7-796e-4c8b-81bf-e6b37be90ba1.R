library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/22af2ab7-796e-4c8b-81bf-e6b37be90ba1.html')