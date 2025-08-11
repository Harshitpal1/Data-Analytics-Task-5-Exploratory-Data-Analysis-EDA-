#Exploratory Data Analysis on the Titanic Dataset
This repository contains the solution for the Task 5: Exploratory Data Analysis (EDA) as part of the Data Analyst Internship selection process for Elevate Labs.

Objective
The primary objective of this project is to perform a thorough exploratory data analysis on the Titanic dataset. The goal is to uncover underlying patterns, identify trends, and extract meaningful insights about the factors that influenced passenger survival during the disaster.

Dataset
The analysis was conducted on the classic Titanic Dataset, which contains demographic and travel information for passengers aboard the Titanic.

Tools and Libraries
Language: Python

Libraries:

Pandas: For data manipulation and cleaning.

Matplotlib & Seaborn: For data visualization and plotting.

Jupyter Notebook: As the development environment.

Analysis Workflow
The EDA was structured around the hints provided in the task description and followed a standard data analysis workflow:

Data Loading and Inspection: The dataset was loaded, and initial inspections were performed using .info(), .describe(), and .value_counts() to understand its structure, identify missing values, and get a statistical summary.

Data Cleaning: Missing values, especially in the 'Age' and 'Embarked' columns, were handled appropriately.

Univariate Analysis: Individual features were analyzed using histograms and count plots to understand their distributions (e.g., age distribution, passenger class distribution).

Bivariate and Multivariate Analysis: Relationships between variables were explored. Key visualizations included:

Bar charts to compare survival rates across different categories (like Gender and Pclass).

Scatter plots to investigate relationships between numerical variables.

A heatmap based on a correlation matrix to quickly identify correlations.

A pairplot to get a comprehensive overview of pairwise relationships.

Insight Generation: Observations were documented for each visual, and a final summary of findings was compiled to explain the factors affecting survival.

Interview Questions & Answers
This section provides answers to the interview questions listed in the task.

1. What is EDA and why is it important?
Exploratory Data Analysis (EDA) is the process of analyzing and visualizing datasets to summarize their main characteristics, uncover patterns, and identify anomalies. It is critically important because it provides the foundational understanding of the data before formal modeling, helping to guide feature engineering, hypothesis testing, and the selection of appropriate analytical techniques.

2. Which plots do you use to check correlation?
To check for correlation, the most effective plots are:

Heatmap: Best for visualizing a correlation matrix of multiple variables.

Scatter Plot: Ideal for examining the relationship between two specific numerical variables.

Pair Plot: Useful for getting a quick overview of pairwise relationships across all numerical variables in a dataset.

3. How do you handle skewed data?
Skewed data can be handled by applying mathematical transformations to make its distribution more symmetric (or "normal-like"). Common techniques include:

Log Transformation: Effective for data with positive skew.

Square Root Transformation: A milder transformation for positive skew.

Box-Cox Transformation: A statistical method that finds the optimal power transformation for the data.

4. How to detect multicollinearity?
Multicollinearity (high correlation between independent variables) can be detected using:

Correlation Matrix: A heatmap can visually reveal high correlation values (e.g., > 0.7 or < -0.7) between variables.

Variance Inflation Factor (VIF): VIF measures how much the variance of a regression coefficient is inflated due to its correlation with other predictors. A VIF score greater than 5 or 10 is often considered problematic.

5. What are univariate, bivariate, and multivariate analyses?
Univariate Analysis: Analyzing a single variable to describe its properties (e.g., histogram, box plot, mean).

Bivariate Analysis: Analyzing two variables to explore their relationship (e.g., scatter plot, bar chart comparing two groups).

Multivariate Analysis: Analyzing three or more variables simultaneously to understand their complex interactions (e.g., 3D scatter plot, correlation heatmap).

6. Difference between heatmap and pairplot?
A heatmap is a single plot that uses color to represent the magnitude of correlation between all pairs of variables in a matrix, providing a quick, high-level summary. In contrast, a pairplot creates a grid of several plots, showing detailed scatterplots for each pairwise relationship and the distribution of each individual variable on the diagonal. It offers a more granular visual inspection.

7. How do you summarize your insights?
To summarize insights effectively, you should:

Start with the most significant findings.

Clearly and concisely state each conclusion.

Support your claims with evidence from your analysis (e.g., "As seen in the bar chart of survival by gender...").

Relate the insights back to the main objective of the analysis.
