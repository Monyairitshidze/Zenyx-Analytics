 

# import panda to prepare data for analysis
import pandas as pd 

# for statistical analysis
import numpy as np



# read file into memeory data
covid_data = pd.read_csv("C:/Users/Ritshidze/OneDrive/Desktop/Analyse Covid-19 Trends/day_wise.csv", header=0, sep=",")

# create data frame to structurer data
df = pd.DataFrame( data = covid_data)

# removing noise 
covid_data.dropna( axis=0 , inplace=True )

# print to check the data types of data for calculation purpose
print(df.info())

# print the summmary of covid data
print(df.describe())

print(df)

# STATISTICS

Confirmed_Cases = covid_data["Confirmed"]

# Claculating the standard deviation of confrimed cases
std = np.std(Confirmed_Cases)

print("The standard deviation is : " + str(std))

# find total
total = Confirmed_Cases.sum()

# find the number of data
no = Confirmed_Cases.count()

# Calculate mean
mean = total / no 


print("The mean is : " + str(mean))

# Calculate coeeficience of Variance

cv = std / mean

print("The coffieence of variation is : " + str(cv))


# Find Varience
varience = np.var(Confirmed_Cases)

print("The varience of confirmed cases is : " + str(varience))







