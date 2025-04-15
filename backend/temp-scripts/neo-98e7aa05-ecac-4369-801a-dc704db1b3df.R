library(ggplot2)
data <- data.frame(x=c(1,2,3), y=c(4,5,6))
p <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')
ggsave('results/neo-98e7aa05-ecac-4369-801a-dc704db1b3df.png', plot=p)