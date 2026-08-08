import pandas as pd

# visualization
import matplotlib.pyplot as plt

# loading dataset
data = pd.read_csv("C:/Users/Ritshidze/Retail Performance analyse/archive (7)/retail_sales_dataset.csv",sep="," ,header=0)

df = pd.DataFrame(data = data)

# "Which age group (e.g., 18-25, 26-35, 36-50, 50+) spends the most overall, and on what category?
def age_segmentation():

    bins = [0, 17, 25, 35, 50, 100]
    labels = ['Under 18', '18-25', '26-35', '36-50', '50+']

    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    result = df.groupby(['Age Group', 'Product Category'])['Total Amount'].sum()

    print("Age Group and Category Spending:")
    print(result)

    print("\nHighest Spending:")
    print(result.idxmax(), result.max())

    result.plot(kind='bar')

    plt.title("Spending by Age Group and Category")
    plt.xlabel("Age Group and Category")
    plt.ylabel("Total Amount")
    plt.show()

# "Which product category generates the most revenue, and which sells the most units (these might differ)?"
def category_performance():

    revenue = df.groupby('Product Category')['Total Amount'].sum()
    quantity = df.groupby('Product Category')['Quantity'].sum()

    print("Revenue by Category:")
    print(revenue)

    print("\nUnits Sold by Category:")
    print(quantity)

    print("\nHighest Revenue Category:")
    print(revenue.idxmax(), revenue.max())

    print("\nHighest Units Sold Category:")
    print(quantity.idxmax(), quantity.max())

    revenue.plot(kind='bar')

    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.show()

    quantity.plot(kind='bar')

    plt.title("Units Sold by Category")
    plt.xlabel("Category")
    plt.ylabel("Quantity")
    plt.show()

# "Which month had the highest sales, and is there a seasonal pattern (e.g., higher in November/December)?"
def time_trend():

    df['Date'] = pd.to_datetime(df['Date'])

    df['Month'] = df['Date'].dt.month

    monthly_sales = df.groupby('Month')['Total Amount'].sum()

    print("Monthly Sales:")
    print(monthly_sales)

    print("\nHighest Sales Month:")
    print(monthly_sales.idxmax(), monthly_sales.max())

    plt.plot(monthly_sales.index, monthly_sales.values)

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.show()

# call the functions
age_segmentation()
category_performance()
time_trend()



