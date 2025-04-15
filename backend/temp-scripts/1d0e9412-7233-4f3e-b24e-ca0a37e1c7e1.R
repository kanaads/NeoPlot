library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/1d0e9412-7233-4f3e-b24e-ca0a37e1c7e1.html')