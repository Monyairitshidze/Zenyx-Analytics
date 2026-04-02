# import pnadas for data preparing
import pandas as pd

# import matplotlib for data visualization
import matplotlib.pyplot as mp

# import stats for analysis
from scipy import stats as st

# read data 
data = pd.read_csv( "day_wise.csv" , header = 0 , sep = "," )

# assign my values to x and y
x = data["Confirmed"]
y = data["Active"]

# linregress will return values and assign them to the variables 1 by 1
slope , intercepts , r , p , error = st.linregress( x , y )

# define a function to predict y
def predictY(x):

    predictedY = slope * x + intercepts

    return predictedY

# create a model that will predict y
# this model predicct y and convert them into a lsit []
predctionModel = list( map( predictY , x ) )

# this is whete where plot 
mp.scatter( x , y)
mp.plot( x , predctionModel)
mp.xlabel("Confirmed")
mp.ylabel("Active")
mp.title("Impact of Confirmed cases on Active Patients")

# show the visualization
mp.show()