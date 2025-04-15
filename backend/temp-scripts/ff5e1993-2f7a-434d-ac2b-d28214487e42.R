library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/ff5e1993-2f7a-434d-ac2b-d28214487e42.html')