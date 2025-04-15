library(ggplot2)

data <- data.frame(x = c("A", "B", "C"), y = c(5, 7, 4))
p <- ggplot(data, aes(x, y)) + 
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  ggtitle("Simple Bar Chart with ggplot2")

ggsave('results/eeb3cad3-8ba4-452f-8591-1cd5e7794789.png', plot=p)