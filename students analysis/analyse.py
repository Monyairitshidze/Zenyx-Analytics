# import pandas for data preparation
import pandas as pd

# import matplotlib for plotiing
import matplotlib.pyplot as plt

# import numpy for statistical analysis
import numpy as np

# IMPORT seaborn for visualization
import seaborn as sn

# import stats for predictive analysis
from scipy import stats

# read data into our programs
students_data = pd.read_csv("Students.csv" , header=0 , sep=",")

# strudcturer data into dataframe
df = pd.DataFrame(data=students_data)

# remove abnromal data
df.dropna(axis=0 ,inplace=True)

# displ;ay all columns
pd.set_option("display.max_columns" , None)

target = "Cumulative grade point average in the last semester (/4.00)"

# /VISUALIZING THE VARIABLES THAT HAVE AN IMPACT OF THE TARGET
variables = []
for col in df.columns:
    if col != target and col != "STUDENT ID":
        variables.append(col)



for var in variables:
    
    plt.figure() 
    plt.title("How " + var + " impacts GPA") 
    plt.xlabel(var) 
    plt.ylabel("GPA") 

    # FIX: ensure numeric data
    x = pd.to_numeric(df[var], errors='coerce')
    y = pd.to_numeric(df[target], errors='coerce')

    plt.scatter(x, y) 
    plt.show()

# /STATISTICAL ANALYSIS/
for col in variables:

    data = pd.to_numeric(df[col], errors='coerce')

    number = data.count()
    mean = data.mean()
    median = data.median()
    std = data.std()

    # percentiles
    q1 = data.quantile(0.25)
    q2 = data.quantile(0.50)
    q3 = data.quantile(0.75)

    variance = data.var()

    if mean != 0:
        cv = (std / mean) * 100
    else:
        cv = None

    print("\nStatistics for:", col)
    print("Number of values:", number)
    print("Mean:", mean)
    print("Median:", median)
    print("Variance:", variance)
    print("Standard deviation:", std)
    print("Coefficient of Variation (%):", cv)
    print("25th percentile:", q1)
    print("50th percentile (median):", q2)
    print("75th percentile:", q3)
    print("")

   
# CORRELATION ANALYSIS
for cor in variables:
    if cor != target and cor != "STUDENT ID":

        data = pd.to_numeric(df[cor], errors='coerce')
        target_data = pd.to_numeric(df[target], errors='coerce')

        std = data.std()
        mean = data.mean()

        if mean != 0:
            cv = std / mean
        else:
            cv = float('inf')

        # (kept your condition but you can relax it if needed)
        if std < 0.5 and cv < 0.5:

            correlation = round(data.corr(target_data), 2)

            print("The correlation of " + cor + " is " + str(correlation))


numeric_df = df.apply(pd.to_numeric, errors='coerce')
corr_matrix = numeric_df.corr()

sn.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

 # /Linear Regression

for var in variables:

    x = pd.to_numeric(df[var], errors='coerce')
    y = pd.to_numeric(df[target], errors='coerce')

    gradient, intercepts, r, p, st_error = stats.linregress(x, y)

    def YPrediction(x):
        return gradient * x + intercepts

    predictive_model = list(map(YPrediction, x))

    plt.figure()
    plt.scatter(x, y, label="Actual Data")
    plt.plot(x, predictive_model, color='red', label="Regression Line")

    plt.xlabel(var)
    plt.ylabel("GPA")
    plt.title("Linear Regression: " + var + " vs GPA")
    plt.legend()

    plt.show()