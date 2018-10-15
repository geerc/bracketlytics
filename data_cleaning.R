install.packages("dplyr")
install.packages("tidyverse")

library(dplyr)
library(tidyverse)

data = read.csv(file = '/Users/Christian/Documents/Bracketlytics/data/2018TeamStats_Final.csv', header = TRUE, sep = ",")
sos.data = read.csv(file = '/Users/Christian/Documents/Bracketlytics/data/sos.csv')

####Compiling game data to season daata####
# Remove uncessary columns
data$gameid <- NULL
data$MP <- NULL
data$FG. <- NULL
data$X2P <- NULL
data$X2PA <- NULL
data$X2P. <- NULL
data$X3PA <- NULL
data$X3P. <- NULL
data$FT. <- NULL
data$TRB <- NULL
data$AST <- NULL
data$STL <- NULL
data$BLK <- NULL
data$PF <- NULL
data$PTS <- NULL
data$Opp.FG. <- NULL
data$Opp.2P <- NULL
data$Opp.2PA <- NULL
data$Opp.2P. <- NULL
data$Opp.3PA <- NULL
data$Opp.3P. <- NULL
data$Opp.FT. <- NULL
data$Opp.TRB <- NULL
data$Opp.AST <- NULL
data$Opp.STL <- NULL
data$Opp.BLK <- NULL
data$Opp.PF <- NULL
data$Opp.PTS <- NULL
data$Win. <- NULL

# Convert columns to numeric data type
data$FG <- as.numeric(as.character(data$FG))
data$FGA <- as.numeric(as.character(data$FGA))
data$X3P <- as.numeric(as.character(data$X3P))
data$FT <- as.numeric(as.character(data$FT))
data$ORB <- as.numeric(as.character(data$ORB))
data$DRB <- as.numeric(as.character(data$DRB))
data$TOV <- as.numeric(as.character(data$TOV))
data$FTA <- as.numeric(as.character(data$FTA))
data$Opp.FG <- as.numeric(as.character(data$Opp.FG))
data$Opp.FGA <- as.numeric(as.character(data$Opp.FGA))
data$Opp.3P <- as.numeric(as.character(data$Opp.3P))
data$Opp.FT <- as.numeric(as.character(data$Opp.FT))
data$Opp.ORB <- as.numeric(as.character(data$Opp.ORB))
data$Opp.DRB <- as.numeric(as.character(data$Opp.DRB))
data$Opp.TOV <- as.numeric(as.character(data$Opp.TOV))
data$Opp.FTA <- as.numeric(as.character(data$Opp.FTA))

# Group individual game data into season data
season.data <- data %>%
  group_by(Team) %>%
  summarise(sum(FG, na.rm = TRUE), sum(FGA, na.rm = TRUE),
            sum(X3P, na.rm = TRUE), sum(FT, na.rm = TRUE),
            sum(FTA, na.rm = TRUE), sum(ORB, na.rm = TRUE),
            sum(DRB, na.rm = TRUE), sum(TOV, na.rm = TRUE),
            sum(Opp.FG, na.rm = TRUE), sum(Opp.FGA, na.rm = TRUE),
            sum(Opp.3P, na.rm = TRUE), sum(Opp.FT, na.rm = TRUE),
            sum(Opp.FTA, na.rm = TRUE), sum(Opp.ORB, na.rm = TRUE),
            sum(Opp.DRB, na.rm = TRUE), sum(Opp.TOV, na.rm = TRUE))

# Rename column hearders
names(season.data)[names(season.data) == "sum(FG, na.rm = TRUE)"] <- "FG"
names(season.data)[names(season.data) == "sum(FGA, na.rm = TRUE)"] <- "FGA"
names(season.data)[names(season.data) == "sum(X3P, na.rm = TRUE)"] <- "X3P"
names(season.data)[names(season.data) == "sum(FT, na.rm = TRUE)"] <- "FT"
names(season.data)[names(season.data) == "sum(FTA, na.rm = TRUE)"] <- "FTA"
names(season.data)[names(season.data) == "sum(ORB, na.rm = TRUE)"] <- "ORB"
names(season.data)[names(season.data) == "sum(DRB, na.rm = TRUE)"] <- "DRB"
names(season.data)[names(season.data) == "sum(TOV, na.rm = TRUE)"] <- "TOV"
names(season.data)[names(season.data) == "sum(Opp.FG, na.rm = TRUE)"] <- "Opp.FG"
names(season.data)[names(season.data) == "sum(Opp.FGA, na.rm = TRUE)"] <- "Opp.FGA"
names(season.data)[names(season.data) == "sum(Opp.3P, na.rm = TRUE)"] <- "Opp.3P"
names(season.data)[names(season.data) == "sum(Opp.FT, na.rm = TRUE)"] <- "Opp.FT"
names(season.data)[names(season.data) == "sum(Opp.FTA, na.rm = TRUE)"] <- "Opp.FTA"
names(season.data)[names(season.data) == "sum(Opp.ORB, na.rm = TRUE)"] <- "Opp.ORB"
names(season.data)[names(season.data) == "sum(Opp.DRB, na.rm = TRUE)"] <- "Opp.DRB"
names(season.data)[names(season.data) == "sum(Opp.TOV, na.rm = TRUE)"] <- "Opp.TOV"

# Reindex
rownames(season.data) <- 1:nrow(season.data)

# Filter out some teams
# season.data <- filter(season.data)

# Save new data as csv file
write.csv(season.data, file = "/Users/Christian/Documents/Bracketlytics/data/season_data.csv")


####Changing Data type of strength of schedule data####

sos.data$SOS <- as.numeric(as.character(sos.data$SOS))
sos.data$Rank <- as.numeric(as.character(sos.data$Rank))
names(sos.data)[names(sos.data) == "School"] <- "Team"


write.csv(sos.data, file = '/Users/Christian/Documents/Bracketlytics/data/sos.csv')

####Joining data####
sos.data$Team <- tolower(sos.data$Team)
full_data = full_join(season.data, sos.data, by = "Team")

sos.data$SOS <- as.numeric(as.character(sos.data$SOS))
sos.data$Rank <- as.numeric(as.character(sos.data$Rank))
names(sos.data)[names(sos.data) == "School"] <- "Team"

sos.data$Team <- tolower(sos.data$Team)
full_data = right_join(season.data, sos.data, by = "Team")

full_data <- na.omit(full_data)

write.csv(sos.data, file = '/Users/Christian/Documents/Bracketlytics/data/season_data.csv')
