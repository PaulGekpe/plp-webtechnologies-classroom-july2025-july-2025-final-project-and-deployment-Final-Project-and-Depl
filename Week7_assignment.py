# -----------------------------------------
# Assignment: Data Analysis & Visualization
# Using Pandas, Matplotlib, and Seaborn
# -----------------------------------------

#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Make plots look nicer
sns.set(style="whitegrid")

# -----------------------------------------
# Task 1: Load and Explore the Dataset
# -----------------------------------------

try:
    # Option 1: Load from sklearn (Iris dataset)
    from sklearn.datasets import load_iris
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame #Already a pandas Dataframe
    df['species'] = df['target'].map(dict(enumerate(iris_data.target_names)))
    
    #Option 2: Load from CSV (Uncomment to use)
    # df = pd.read_csv('path_to_your_file.csv')

    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: file was not found. please check the file path")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    
    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Dataset info
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (if needed)
    df = df.dropna() # or df.fillna(value, inplace=True)

# -----------------------------------------
# Task 2: Basic Data Analysis
# -----------------------------------------

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping example: average petal length per species
grouped = df.groupby('species')['petal length (cm)'].mean()
print("\nAverage Petal Length per Species:")
print(grouped)

# Example observations
print("\nObservations: The species with the largest average petal length is:",
grouped.idxmax())

# -----------------------------------------
# Task 3: Data Visualization
# -----------------------------------------

# 1️⃣ Line Chart - Example: petal length trend by index
plt.figure(figsize=(8,5))
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Petal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar Chart - Average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3️⃣ Histogram - Distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# -----------------------------------------
# Findings / Observations
# -----------------------------------------
"""
1. Petal length varies significantly between species, with 'virginica' having the longest average petals.
2. Sepal width distribution is roughly normal but slightly skewed.
3. Scatter plot shows clear clustering of species based on sepal and petal measurements.
4. Line chart shows no obvious time trend (since this dataset isn't time-based), but demonstrates plotting capability.
"""