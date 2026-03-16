 

# import panda to prepare data for analysis
import pandas as pd 

# for ploting
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

# convert date column
covid_data["Date"] = pd.to_datetime(covid_data["Date"])

# choosing table to plot
covid_data.plot(x ="Date", y = ["Deaths","Recovered","Active"],kind="line")

mp.ylim(0 , 170000000)
mp.xlim(0 , 170000000)

mp.show()







