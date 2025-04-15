library(ggplot2)
data <- data.frame(x=c(1,2,3), y=c(4,5,6))
p <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')
ggsave('results/1f5387bd-8dda-4133-b5c3-4c19696cb921.png', plot=p)