

require( ggplot2 )

univ <- read.csv( 'map.csv' )
p    <- ggplot( univ, aes(x, y, label=name) ) + 
        geom_point() +
        geom_text( hjust=0, vjust=0 )

ggsave( plot=p, 'map.png' )
