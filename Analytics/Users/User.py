
import pandas as pd 

# importing data 
data = pd.read_csv('C:/Users/Ritshidze/OneDrive/Desktop/CSS/main/country_data.csv',index_col=0)

# creating a dataframe that help to structurer our data
dataframe = pd.DataFrame(data=data)

dataframe.dropna(inplace=True)

# printing the data
print(dataframe)