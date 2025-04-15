library(plotly)
p <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')
htmlwidgets::saveWidget(p, 'results/0cc8e834-4aef-43f4-a09d-5864fc846b5e.html')