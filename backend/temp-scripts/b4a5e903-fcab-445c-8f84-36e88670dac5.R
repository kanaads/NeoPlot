library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/b4a5e903-fcab-445c-8f84-36e88670dac5.html')