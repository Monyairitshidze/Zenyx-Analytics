# import pandas to structurer data
import pandas as pd

# import for data visualization
import matplotlib.pyplot as mp

# import numpy for statistical analysis
import numpy as np

# import seaborn for visualization
import seaborn as sb

# import scipy for linear regression
from scipy import stats

# import stats for regresiion table
import statsmodels.formula.api as sfa

# /DATA PREPARATION/
# read data into our code 
full_data = pd.read_csv( "day_wise.csv" , header = 0 , sep = "," )

# structurer our data into a dataframe
dataFrame = pd.DataFrame( data = full_data )

# remove abnromal data
dataFrame.dropna( axis = 0 , inplace = True )

# /FIND SUMMARY OF THE ENTIRER DATASET/
print(dataFrame.describe())

# /STATISTICAL ANALYSIS/
# choose a column to work with 
x = dataFrame["Recovered"]
y = dataFrame["Active"]

# find the percebntile of 25
perX = np.percentile(x , 25)
# display the results
print("The percentile of 25" + str(perX))

# find the percebntile of 25
perY = np.percentile(y , 25)
# display the results
print("The percentile of 25" + str(perY))

# find the stndad deviation of the 2
stdX = np.std(x)

stdY = np.std(y)

# print the standard deviation
print("The standard deviation of Recoverd : " + str(stdX))
print("The standard deviation of Active : " + str(stdY))

#  variation
# this is another value that shows us how scatterd our values are
varX = np.var(x)

varY = np.var(y)

# print the standard deviation
print("The variation of Recoverd : " + str(varX))
print("The variation of Active : " + str(varY))

# this help us to see how big is our standard deviation
# find the total number of values
countX = x.count()
countY = y.count()

# get the values in x 1 at a time
totalX = 0
for i in x:

    totalX += i

# find the values in y  1 at a time
totalY = 0
for i in y :
    
    totalY += i

meanX = totalX / countX

meanY = totalY / countY

# the mean for x and y are as follows
print("The mean for x is :" + str(meanX))
print("The mean for y is :" + str(meanY))

# /Visualize the data/
mp.plot(x,y)
mp.ylabel("Active")
mp.xlabel("Recovered")
mp.title("The impact that Recoverd people have on Active people")

# /RELATIONSHIP BETWEEN TWO VAIABLES USING CORELATION/
# check wetaher the twoo variables have an impact on each other 

mp.scatter(x , y)
mp.plot( x ,y)
mp.ylabel("Active")
mp.xlabel("Recovered")
mp.title("The impact that Recoverd people have on Active people")


# create corelation matrix 
coreMatrix = round( dataFrame.select_dtypes(include = "number").corr(), 2)

print(coreMatrix)

# using a heapmap

corr = sb.heatmap(

coreMatrix,
vmin = -1 , vmax =1 , center= 0,
cmap = sb.diverging_palette(50,500, n = 500),
square = True

)

mp.show()

# /DOING LINEAR REGRESSION/
slope , intercept , r , p  , error = stats.linregress(x , y)

# define a function to predict y
def predictY( x ):

    predictedY = slope * x + intercept

    return predictedY


# create a model to predicty y
predictionModel = list( map( predictY , x) )

mp.scatter(x , y)
mp.plot( x ,predictionModel)
mp.ylabel("Active")
mp.xlabel("Recovered")
mp.title("The impact that Recoverd people have on Active people")
mp.show()

# Regression Table
regTable = sfa.ols(" Recovered ~ Active" , data = dataFrame)

results = regTable.fit()

print(results.summary())

