library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/9a4cf706-dcdd-4af1-a972-2f048ebcb1f0.html')