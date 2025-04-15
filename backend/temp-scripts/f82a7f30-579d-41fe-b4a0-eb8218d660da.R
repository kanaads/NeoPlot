library(ggplot2)

data <- data.frame(x = c("A", "B", "C"), y = c(5, 7, 4))
p <- ggplot(data, aes(x, y)) + 
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  ggtitle("Simple Bar Chart with ggplot2")
