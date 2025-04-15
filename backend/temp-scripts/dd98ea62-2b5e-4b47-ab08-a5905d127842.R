library(ggplot2)
data <- data.frame(x=c(1,2,3), y=c(4,5,6))
p <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')
ggsave('results/dd98ea62-2b5e-4b47-ab08-a5905d127842.png', plot=p)