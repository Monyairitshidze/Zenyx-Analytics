# import pandas for data prepaqration
import pandas as pd 

# import matplotlib for data visualization
import matplotlib.pyplot as mp 

# reading the data
coutry_data =  pd.read_csv("day_wise.csv", header=0 , sep=",")

# structurer the data into dataframe
df = pd.DataFrame( data = coutry_data)

# remove abnormal values 
df.dropna( axis = 0 , inplace= True )

# plot the correlation 
coutry_data.plot( x = "Recovered" , y = "Active" , kind = "scatter")

# display the graphics
mp.show()
