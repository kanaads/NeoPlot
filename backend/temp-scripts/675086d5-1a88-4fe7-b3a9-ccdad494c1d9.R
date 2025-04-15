library(ggplot2)

data <- data.frame(x = c("A", "B", "C"), y = c(5, 7, 4))
p <- ggplot(data, aes(x, y)) + 
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  ggtitle("Simple Bar Chart with ggplot2")

ggsave('results/675086d5-1a88-4fe7-b3a9-ccdad494c1d9.png', plot=p)