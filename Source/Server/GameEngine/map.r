
require(ggplot2)
univ <- read.csv('map.csv')
p <- ggplot(univ,aes(x,y))+geom_point()
ggsave(plot=p, 'map.pdf')
