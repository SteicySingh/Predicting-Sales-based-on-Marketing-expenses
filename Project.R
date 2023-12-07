LRData_Analysis <- read.csv ("/Users/steicysingh/Desktop/Spring 2023/INST737/Final Project/Final Model/Dataset.csv")
LRData_Analysis
attach(LRData_Analysis)

library(graphics)

summary(TV)
sd(TV)

summary(Radio)
sd(Radio)


summary(SocialMedia)
sd(SocialMedia)

summary(Sales)
sd(Sales)

class(Radio)
class(SocialMedia)
class(Sales)


plot(LRData_Analysis$TV, LRData_Analysis$Sales, ylab = "Sales in Millions", xlab = "TV Budget in Millions")
cor.test(LRData_Analysis$SocialMedia, LRData_Analysis$Radio)

plot(LRData_Analysis$Radio, LRData_Analysis$Sales, ylab = "Sales in Millions", xlab = "Radio Budget in Millions")
cor.test(LRData_Analysis$Radio, LRData_Analysis$Sales)

plot(LRData_Analysis$SocialMedia, LRData_Analysis$Sales, ylab = "Sales in Millions", xlab = "Social Media Budget in Millions")
cor.test(LRData_Analysis$SocialMedia, LRData_Analysis$Sales)




