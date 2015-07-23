fp = "/home/admin123/MLExperiments/LSH/house-votes-84.csv"
hvdf = read.table(fp, na.strings = "?", sep = ",")
#hvdf = hvdf[complete.cases(hvdf),]
col.names = c("D/R", "handicapped-infants", "water-project-cost-sharing",
              "adoption-of-the-budget-resolution", "physician-fee-freeze", 
              "el-salvador-aid", "religious-groups-in-schools",
              "anti-satellite-test-ban","aid-to-nicaraguan-contras",
              "mx-missile", "immigration","synfuels-corporation-cutback",
              "education-spending","superfund-right-to-sue", "crime",
              "duty-free-exports", "export-administration-act-south-africa")
names(hvdf) = col.names

# Recode variables to 0 and 1 from yes and no - just makes implementation of LSH easier
library(dummies)
ddf = dummy.data.frame(hvdf, names = col.names, sep = "#")


fp2  = "/home/admin123/MLExperiments/LSH/cvr_clean.csv"
write.csv(ddf, fp2, row.names = FALSE,)