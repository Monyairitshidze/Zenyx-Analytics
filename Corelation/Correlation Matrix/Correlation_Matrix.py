
# import pandas to prepare data 
import pandas as pd 

# import matloplib to diplay visualization
import matplotlib.pyplot as mp

# import seaborn for data visualization
import seaborn as sb

# import data 
daily_wise = pd.read_csv("day_wise.csv" , header= 0 , sep= ",")

# structurer data in data frames 
df = pd.DataFrame( data = daily_wise )

# remove abronal data 
df.dropna( axis= 0 , inplace= True)

# Create a correaltion matrix 
correlation_Matrix = round( df.select_dtypes( include = "number").corr() , 2 )

#  print matrix 
print(correlation_Matrix)

# visualise the matrix 
axis_corr = sb.heatmap(

correlation_Matrix,
vmin = -1 ,
 vmax = 1 ,
   center = 0,
cmap = sb.diverging_palette( 
    50 ,
      500 , 
      n = 500 ),
      square = True

)

# display visuyalization uisng matplotlib
mp.show()