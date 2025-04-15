library(ggplot2)

data <- data.frame(x = c("A", "B", "C"), y = c(5, 7, 4))
p <- ggplot(data, aes(x, y)) + 
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  ggtitle("Simple Bar Chart with ggplot2")

ggsave('results/12d86cd5-b000-46c8-9910-be3a801ae341.png', plot=p)