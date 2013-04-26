

require( ggplot2 )

univ <- read.csv( 'map.csv' )
univ$owner <- factor( univ$owner )

p    <- ggplot( univ, aes(x, y, label=name, size=size) ) + 
        geom_point( aes(color=owner ) ) +
        geom_text( hjust=0, vjust=0 ) + scale_colour_brewer(palette="Set1")

ggsave( plot=p, 'map.png' )
