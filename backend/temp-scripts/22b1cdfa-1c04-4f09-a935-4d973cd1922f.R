library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/22b1cdfa-1c04-4f09-a935-4d973cd1922f.html')