##

library(tidyverse)
library(scales)
library(gganimate)
library(gifski)


x <- read.csv("unemployment.csv", header=TRUE)

str(x)
str(x$date2)

x$date3 <- as.Date(x$date2, format = "%m/%d/%Y")

options(scipen=10000)

fig <- ggplot(data=x, aes (x=date3, y =nsa2)) +  
  geom_line(color = "orangered1", size = 1) + 
  xlab("Date") + ylab("Initial unemployment insurance claims") + 
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(), axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=22, family="Helvetica"))   +
  scale_x_date(breaks = pretty_breaks(8)) +
  scale_y_continuous(label=comma) +
  theme(axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)))
fig

anim <- fig +
  transition_reveal(date3)

animate(anim, renderer = gifski_renderer(),
       width= 600, height=500, end_pause = 20)
anim_save("un_example.gif")


anim2 <- fig + transition_reveal(date3) + view_follow()
animate(anim2, renderer = gifski_renderer(),
        width= 800, height=450, end_pause = 40,
        duration = 15)
anim_save("un_example2.gif")


