"""Objective For this Assignment:

To load and analyze a dataset using the pandas library in Python.
To create simple plots and charts with the matplotlib library for visualizing the data.



Submission Requirements
Submit a Jupyter notebook (.ipynb file) or Python script (.py file) containing:
Data loading and exploration steps.
Basic data analysis results.
Visualizations.
Any findings or observations

Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset,
 a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.
Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, 
or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.



Additional Instructions

Dataset Suggestions:

You can use publicly available datasets from sites like Kaggle or UCI Machine Learning Repository.
The Iris dataset (a classic dataset for classification problems) 
can be accessed via sklearn.datasets.load_iris(), which can be used for the analysis.

Plot Customization:

Customize the plots using the matplotlib library to add titles, axis labels, and legends.
Use seaborn for additional plotting styles, which can make your charts more visually appealing.

Error Handling:

Handle possible errors during the file reading (e.g., file not found), 
missing data, or incorrect data types by using exception-handling mechanisms (try, except).

Submission:

Ensure your submission is complete with all necessary code and explanations.
 Make sure that each plot is properly labeled and provides insights into the dataset.






"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
# Load the dataset
try:
    df = pd.read_csv('sales_data.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("File not found. Please ensure the dataset file is in the correct directory.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Display the first few rows
print("\nFirst Few Rows of the Dataset:")
print(df.head())

# Display dataset structure and missing values
print("\nDataset Information:")
print(df.info())
print("\nMissing Values Count:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Basic statistics of numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Grouping by 'Category' and calculating the average 'Units Sold'
category_group = df.groupby('Category')['Units Sold'].mean()
print("\nAverage Units Sold per Category:")
print(category_group)

# Task 3: Data Visualization
# Line Chart: Total Revenue over Date
plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(df['Date']), df['Total Revenue'], marker='o', label='Total Revenue')
plt.title('Total Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart: Average Units Sold per Category
plt.figure(figsize=(10, 6))
sns.barplot(x=category_group.index, y=category_group.values, palette='viridis')
plt.title('Average Units Sold by Category')
plt.xlabel('Category')
plt.ylabel('Average Units Sold')
plt.show()

# Histogram: Distribution of Unit Price
plt.figure(figsize=(10, 6))
plt.hist(df['Unit Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Unit Prices')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Units Sold vs. Total Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Total Revenue', data=df, hue='Category', palette='deep')
plt.title('Units Sold vs. Total Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Total Revenue')
plt.legend(title='Category')
plt.show()

# Task 4: Observations and Insights
print("\nObservations and Insights:")
print("1. Total Revenue shows steady variation over the time period in the dataset.")
print("2. Food and Personal Care categories have higher average Units Sold compared to others.")
print("3. Unit Prices are concentrated mostly between $1 and $8.")
print("4. A strong positive correlation exists between Units Sold and Total Revenue.")

