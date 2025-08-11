# Data-Analytics-Task-5-Exploratory-Data-Analysis-EDA-
ask 5: Exploratory Data Analysis (EDA) 

This repository contains the work for the Data Analyst Internship task focused on Exploratory Data Analysis.

Objective
The primary goal is to analyze a dataset to extract insights using visual and statistical exploration techniques.

Dataset
The analysis was performed on the 

Titanic Dataset.

Tools Used
Python 

Pandas 

Matplotlib 

Seaborn 

Interview Questions 

Below are the answers to the interview questions listed in the task.

1. What is EDA and why is it important? 


Exploratory Data Analysis (EDA) is the process of investigating datasets to summarize their main characteristics, often using data visualization and statistical methods. It is important because it helps to identify patterns, spot anomalies, test hypotheses, and check assumptions before formal modeling.

2. Which plots do you use to check correlation? 


To check for correlation, the most common plots are:


Heatmaps: Excellent for visualizing the correlation matrix of multiple variables at once.


Scatterplots: Used to visualize the relationship between two specific numerical variables.


Pairplots: Creates a grid of scatterplots to show pairwise relationships between several variables in a dataset.

3. How do you handle skewed data? 


Skewed data can be handled by applying mathematical transformations to make its distribution more symmetrical (or normal). Common techniques include:

Log transformation

Square root transformation

Box-Cox transformation

4. How to detect multicollinearity? 


Multicollinearity (high correlation between independent variables) can be detected using:

Correlation Matrix: A heatmap can visually expose high correlation values between variables.

Variance Inflation Factor (VIF): VIF is a score that quantifies the severity of multicollinearity in a regression analysis. A high VIF (often > 5 or 10) indicates a problem.

5. What are univariate, bivariate, and multivariate analyses? 

Univariate Analysis: Analyzing a single variable at a time to understand its distribution and characteristics. Examples include histograms and boxplots.

Bivariate Analysis: Analyzing two variables to explore the relationship between them. Examples include scatterplots and correlation heatmaps.

Multivariate Analysis: Analyzing three or more variables simultaneously to understand their complex interactions. A pairplot is an example of a visualization used for this purpose.

6. Difference between heatmap and pairplot? 

Heatmap: A heatmap is a single plot that uses color to represent the magnitude of the correlation between every pair of variables in a dataset. It provides a quick, high-level summary of relationships.

Pairplot: A pairplot creates a grid of plots. It shows scatterplots for the relationships between each pair of variables and the distribution (usually a histogram) of each single variable on the diagonal. It provides a more detailed, granular view of both distributions and relationships.

7. How do you summarize your insights? 


To summarize insights, you should:

State the key findings clearly and concisely.

Relate the findings back to the objective of the analysis.

Use observations from visuals (plots, charts) and statistical tests as evidence.

Highlight any identified trends, patterns, or anomalies discovered during the exploration.
