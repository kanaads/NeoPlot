library(ggplot2)
data <- data.frame(x=c(1,2,3), y=c(4,5,6))
p <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')
ggsave('results/cb65ed89-d113-4c73-a72e-423bb21e4820.png', plot=p)