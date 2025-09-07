'''
Python Libraries Assignment
Author: Paul Kelechi Gekpe
Date: September 2025
Description:
Demonstrates the use of Python's Standard Library, NumPy, Pandas, and Matplotlib.
'''
#---------------
# 1. Python Standard Library
#---------------
import math
import random
from datetime import datetime

print("=== Python Standard Library Examples ===")
# Math module
number = 49
print("Square root of {number} is:", math.sqrt(number))

#Random module
print("Random number between 1 and 100:", random.randint(1, 100))

# Datetime module
current_time = datetime.now()
print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

#---------------
# 2. NumPy
#---------------
import numpy as np

print("\n=== NumPy Examples ===")
# Creating a NumPy array
arr = np.array([10, 20 , 30 , 40 , 50 ])
print("Array:", arr)

# Perform calculations
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Array multiplied by 2:", arr * 2)

#---------------
# 3. Pandas
#---------------
import pandas as pd
print("\n=== Pandas Examples ===")
# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Score': [85, 90, 78, 92],
    'Age': [20, 21, 19, 22]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

#Filter data
high_scorers = df[df['Score'] > 80]
print("\nStudents with scores above 80:\n", high_scorers)

#Summary statistics
print("\nAverage Score:", df['Score'].mean())

# -----------------------------
# 4. Matplotlib
# -----------------------------
import matplotlib.pyplot as plt

print("\n=== Matplotlib Example ===")
# Create a bar chart of scores
plt.figure(figsize=(6, 4))
plt.bar(df['Name'], df['Score'], color='skyblue', edgecolor='black')
plt.title('Student Scores')
plt.xlabel('Name')
plt.ylabel('Score')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()