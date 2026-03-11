# analyse the countreywise data

# import panda to prepare data for analysis
import pandas as pd 

import matplotlib.pyplot as mp


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

# print to know tables on the files 
print(df.head())





