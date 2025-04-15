library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/84161806-dd06-4886-b2da-9f7dfce55a53.html')