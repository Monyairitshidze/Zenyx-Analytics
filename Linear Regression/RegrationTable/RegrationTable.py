
# import stats function to fins the regration tables
import statsmodels.formula.api as sfa

# import pandas to structurer data
import pandas as pd

# import matplotlib for visualization
import matplotlib.pyplot as mp

# read data
day_wise = pd.read_csv( "day_wise.csv" , header = 0 , sep = "," )

# create a dataframe to structurer data
df = pd.DataFrame( data = day_wise)

# drop abnromal data
df.dropna( inplace = True , axis = 0 )

# create a model to find linear regression
model = sfa.ols( "Confirmed ~ Active" , data = df )

# calculate all the values like intercepts etc
results = model.fit()

# summarise the results
summary = results.summary()

# display the summary
print(summary)

# select the active adat set only
Active = df["Active"]

# find the linear regresiio funcion by coef 
confirmed = 2.3831 * Active -6.219e+05
print(confirmed)

# find the p - value
# since the p valut is < 0.05 this tells us the relationship exists meaning we reject the H0(null hypotheisi)

# find the R SQURED
# since the r and adj squred are 0.973 this tells us that the many data points are close to the linear regression function line.
