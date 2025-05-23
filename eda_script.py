import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directory for saving plots
os.makedirs("images", exist_ok=True)

# Load dataset
data = pd.read_csv("bankmarketingdata.csv")

# Display basic info
print("First 5 rows of the dataset:")
print(data.head())

# Handling missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Fill missing values
data.fillna(method='ffill', inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(data.describe(include='all'))

# Visualization examples

# 1. Age distribution
if 'age' in data.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(data['age'], kde=True, bins=30)
    plt.title('Age Distribution')
    plt.savefig("images/age_distribution.png")
    plt.close()

# 2. Job count plot
if 'job' in data.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(y='job', data=data, order=data['job'].value_counts().index)
    plt.title('Job Distribution')
    plt.savefig("images/job_distribution.png")
    plt.close()

# 3. Education pie chart
if 'education' in data.columns:
    plt.figure(figsize=(6, 6))
    data['education'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Education Distribution')
    plt.ylabel('')
    plt.savefig("images/education_pie.png")
    plt.close()

# 4. Loan vs Age scatter plot
if 'loan' in data.columns and 'age' in data.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='loan', y='age', data=data)
    plt.title('Loan vs Age')
    plt.savefig("images/loan_vs_age.png")
    plt.close()

print("\nEDA completed. Plots are saved in the 'images' folder.")
