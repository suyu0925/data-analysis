setwd('./lesson2')
reddit = read.csv('reddit.csv')

str(reddit)

# table(reddit$employment.status)
summary(reddit)

levels(reddit$age.range)
reddit$age.range.order <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34",
                                                               "35-44", "45-54", "55-64", "65 or Above"))

library('ggplot2')
qplot(data = reddit, x = age.range.order)
