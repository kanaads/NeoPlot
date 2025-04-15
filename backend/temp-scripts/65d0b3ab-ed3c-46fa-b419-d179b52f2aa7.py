library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/65d0b3ab-ed3c-46fa-b419-d179b52f2aa7.html')