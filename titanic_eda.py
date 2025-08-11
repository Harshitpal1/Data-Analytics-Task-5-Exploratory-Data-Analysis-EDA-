# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Data Loading and Initial Inspection ---

# Load the Titanic dataset from the provided CSV file
# Make sure 'Titanic-Dataset.csv' is in the same directory as your script/notebook.
try:
    df = pd.read_csv('Titanic-Dataset.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: 'Titanic-Dataset.csv' not found. Please check the file path.")
    exit()


print("\n--- Initial Data Overview ---")
# Display the first 5 rows to get a feel for the data
print("First 5 Rows:")
print(df.head())
print("\n" + "="*50 + "\n")

# Get a concise summary of the dataframe
# This is useful for seeing data types and non-null counts.
print("DataFrame Info:")
df.info()
print("\n" + "="*50 + "\n")

# Generate descriptive statistics for numerical columns
print("Descriptive Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Check for the total number of missing values in each column
print("Missing Values per Column:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")


# --- 2. Data Cleaning ---

# Handle missing values.
# For 'Age', we can fill missing values with the median age of the dataset.
# The median is often better than the mean for skewed distributions.
df['Age'].fillna(df['Age'].median(), inplace=True)

# For 'Embarked', the number of missing values is small. We can fill them
# with the mode (the most common embarkation point).
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# The 'Cabin' column has a large number of missing values (687 out of 891).
# It's difficult to impute this meaningfully. For this analysis, we will drop it.
# A more advanced analysis might try to extract features from it (e.g., the deck letter).
df.drop('Cabin', axis=1, inplace=True)


print("--- Data After Cleaning ---")
print("Missing Values After Cleaning:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")


# --- 3. Exploratory Data Analysis & Visualization ---

# Set the style for the plots
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

# a. Univariate Analysis (Analyzing single variables)

# Plotting a histogram for Age
print("Generating Histogram for Age Distribution...")
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()
# Observation: The majority of passengers were young adults between 20 and 40.

# Plotting a count plot for Sex
print("Generating Count Plot for Gender...")
sns.countplot(x='Sex', data=df)
plt.title('Gender Distribution of Passengers')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
# Observation: There were significantly more male passengers than female passengers.

# Plotting a count plot for Pclass
print("Generating Count Plot for Passenger Class...")
sns.countplot(x='Pclass', data=df)
plt.title('Passenger Class Distribution')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()
# Observation: The 3rd class had the most passengers, followed by 1st and 2nd.

# b. Bivariate Analysis (Analyzing relationships between two variables)

# Survival rate by Sex
print("Generating Survival Count by Gender...")
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.legend(title='Sex')
plt.show()
# Observation: Females had a much higher survival rate than males.

# Survival rate by Pclass
print("Generating Survival Count by Passenger Class...")
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival Count by Passenger Class')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.legend(title='Passenger Class')
plt.show()
# Observation: Passengers in 1st class had a higher survival rate than those in 2nd and 3rd class.

# Scatter plot for Age vs. Fare
print("Generating Scatter Plot for Age vs. Fare...")
sns.scatterplot(x='Age', y='Fare', data=df, hue='Survived')
plt.title('Scatter Plot of Age vs. Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
# Observation: No strong linear relationship, but higher fares seem to have a slightly better survival rate.

# c. Multivariate Analysis (Analyzing multiple variables)

# Correlation Heatmap
# We need to select only numerical columns for the correlation matrix.
numerical_cols = df.select_dtypes(include=np.number)
correlation_matrix = numerical_cols.corr()

print("Generating Correlation Heatmap...")
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()
# Observation: 'Pclass' and 'Fare' have a strong negative correlation. 'Pclass' and 'Survived' also show a negative correlation.

# Pairplot to see pairwise relationships
# A pairplot can be computationally intensive, so we select a subset of columns.
print("Generating Pairplot...")
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare', 'Sex']], hue='Survived', diag_kind='kde')
plt.suptitle('Pairwise Relationships of Key Features', y=1.02)
plt.show()
# Observation: The pairplot confirms findings from other plots, showing clear separation in survival based on sex and pclass.

print("\n--- EDA Complete ---")
