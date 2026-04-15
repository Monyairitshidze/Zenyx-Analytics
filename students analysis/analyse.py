# import pandas for data preparation
import pandas as pd

# import matplotlib for plotiing
import matplotlib.pyplot as plt

# read data into our programs
students_data = pd.read_csv("students.csv" , header=0 , sep=",")

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

for var in variables:

    plt.figure()
    plt.title("How " + var + " impacts GPA")
    plt.xlabel(var)
    plt.ylabel("GPA")
    plt.scatter(df[var], df[target])
    plt.show()