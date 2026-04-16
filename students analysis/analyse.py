# import pandas for data preparation
import pandas as pd

# import matplotlib for plotiing
import matplotlib.pyplot as plt

# import numpy for statistical analysis
import numpy as np

# read data into our programs
students_data = pd.read_csv("Students.csv" , header=0 , sep=",")

# strudcturer data into dataframe
df = pd.DataFrame( data= students_data)

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



# /STATISTICAL ANALYSIS/
# STATISTICAL ANALYSIS
for col in variables:

    # convert column to numeric (important for safety)
    data = pd.to_numeric(df[col], errors='coerce')

    number = data.count()  # number of valid values
    mean = data.mean()
    median = data.median()
    std = data.std()

    # 25th, 50th, 75th percentiles
    q1 = data.quantile(0.25)
    q2 = data.quantile(0.50)  # same as median
    q3 = data.quantile(0.75)
    variance = data.var()


    # avoid division by zero for CV
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