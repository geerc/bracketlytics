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

write.csv(full_data, file = '/Users/Christian/Documents/Bracketlytics/data/season_data.csv')

####Linear Regression Data conversion and joining####
Off_2017_2018 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2017-18.csv', header = TRUE, sep = ",")
Off_2016_2017 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2016-17.csv', header = TRUE, sep = ",")
Off_2015_2016 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2015-16.csv', header = TRUE, sep = ",")
Off_2014_2015 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2014-15.csv', header = TRUE, sep = ",")
Off_2013_2014 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2013-14.csv', header = TRUE, sep = ",")

Def_2017_2018 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Def_2017-18.csv', header = TRUE, sep = ",")
Def_2016_2017 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Def_2017-18.csv', header = TRUE, sep = ",")
Def_2015_2016 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Def_2017-18.csv', header = TRUE, sep = ",")
Def_2014_2015 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Def_2017-18.csv', header = TRUE, sep = ",")
Def_2013_2014 = read.csv(file <- '/Users/Christian/Documents/Bracketlytics/data/model_data/Def_2017-18.csv', header = TRUE, sep = ",")

# Join offensive and defensive files together
total_2017_2018 <- full_join(Off_2017_2018, Def_2017_2018, by = "School")
total_2016_2017 <- full_join(Off_2016_2017, Def_2016_2017, by = "School")
total_2015_2016 <- full_join(Off_2015_2016, Def_2015_2016, by = "School")
total_2014_2015 <- full_join(Off_2014_2015, Def_2014_2015, by = "School")
total_2013_2014 <- full_join(Off_2013_2014, Def_2013_2014, by = "School")

# Add year to school names
total_2017_2018 <- transform(total_2017_2018, School = sprintf('%s_2018', School)) 
total_2016_2017 <- transform(total_2016_2017, School = sprintf('%s_2017', School)) 
total_2015_2016 <- transform(total_2015_2016, School = sprintf('%s_2016', School)) 
total_2014_2015 <- transform(total_2014_2015, School = sprintf('%s_2015', School)) 
total_2013_2014 <- transform(total_2013_2014, School = sprintf('%s_2014', School)) 

# Add NCAA tournament wins for each team
wins_2018 <- read_csv("/Users/Christian/Documents/Bracketlytics/data/model_data/wins.csv")
total_2017_2018 <- full_join(total_2017_2018, wins_2018, by = "School")

# Append data sets to each other
full_data <- full_join(total_2017_2018, total_2016_2017, by = NULL) %>%
  full_join(total_2015_2016, by = NULL) %>%
  full_join(total_2015_2016, by = NULL) %>%
  full_join(total_2014_2015, by = NULL) %>%
  full_join(total_2013_2014, by = NULL)

total_2017_2018$School = gsub(" ID.*","",total_2017_2018$School)

####Convert data to float####

data = read.csv(file = '/Users/Christian/Documents/Bracketlytics/data/2018TeamStats_Final.csv', header = TRUE, sep = ",")

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

# Create new four factors stats and round
data$eFG = (data$FG + 0.5 * data$X3P) / data$FGA
data$OeFG = (data$Opp.FG + 0.5 * data$Opp.3P) / data$Opp.FGA
data$eFG = round(data$eFG, digits = 3)
data$OeFG = round(data$OeFG, digits = 3)

data$TOVp = data$TOV / (data$FGA + 0.44 + data$FTA + data$TOV)
data$oTOVp = data$Opp.TOV / (data$Opp.FGA + 0.44 + data$Opp.FTA + data$Opp.TOV)
data$TOVp = round(data$TOVp, digits = 3)
data$oTOVp = round(data$oTOVp, digits = 3)

data$ORBp = data$ORB / (data$ORB + data$Opp.DRB)
data$DRBp = data$DRB / (data$DRB + data$Opp.DRB)
data$ORBp = round(data$ORBp, digits = 3)
data$DRBp = round(data$DRBp, digits = 3)


write.csv(data, file = "/Users/Christian/Documents/Bracketlytics/data/game_data.csv")


