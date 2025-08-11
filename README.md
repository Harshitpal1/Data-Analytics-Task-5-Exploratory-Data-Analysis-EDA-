# Task 5: Exploratory Data Analysis (EDA)  
**Data Analyst Internship – Elevate Labs**  

## 📌 Objective  
Perform a comprehensive Exploratory Data Analysis (EDA) on the Titanic dataset to extract meaningful insights using statistical and visual exploration techniques.  

---

## 📂 Dataset  
- **Name:** Titanic Dataset (as recommended in task description)  
- **Source:** Provided by Elevate Labs  
- **Description:** Passenger details such as demographics, ticket class, fare, and survival status.  

---

## 🛠 Tools Used  
- **Python** – Data analysis and scripting  
- **Pandas** – Data manipulation and inspection  
- **Matplotlib** – Data visualization  
- **Seaborn** – Advanced and aesthetic plotting  

---

## 🔍 EDA Process  

### **1. Initial Data Inspection**
- `.info()` – Data types and missing values  
- `.describe()` – Statistical summaries  
- `.value_counts()` – Categorical variable distributions  

### **2. Data Visualization**
- **Histograms** – Numerical distributions  
- **Boxplots** – Outlier detection  
- **Scatterplots** – Relationship analysis  
- **Heatmap** – Correlation identification  
- **Pairplot** – Pairwise relationships and distributions  

### **3. Key Insights**
- Females had a significantly higher survival rate than males.  
- Passengers in higher classes had better survival rates.  
- Younger passengers had slightly better survival chances.  
- Higher fares correlated with better survival probability.  

---

## 💬 Interview Q&A  

**1. What is EDA and why is it important?**  
EDA is the process of summarizing a dataset’s main characteristics through statistics and visualizations. It helps identify patterns, anomalies, and trends before modeling.  

**2. Which plots do you use to check correlation?**  
- Heatmap (correlation matrix)  
- Scatterplot (two numerical variables)  
- Pairplot (multiple scatterplots for all pairs)  

**3. How do you handle skewed data?**  
- Log Transformation  
- Square Root Transformation  
- Box-Cox Transformation  

**4. How to detect multicollinearity?**  
- Correlation Matrix (Heatmap)  
- Variance Inflation Factor (VIF > 5 or 10)  

**5. What are univariate, bivariate, and multivariate analyses?**  
- **Univariate**: One variable (e.g., histogram)  
- **Bivariate**: Two variables (e.g., scatterplot)  
- **Multivariate**: More than two variables (e.g., pairplot)  

**6. Difference between Heatmap and Pairplot?**  
- **Heatmap**: Color-coded summary of correlations in a matrix.  
- **Pairplot**: Scatterplots and distributions for each pair of variables.  

**7. How do you summarize insights?**  
State key findings, link them to objectives, and support them with evidence from visuals and statistics.  

---

## 📊 Final Summary of Findings  
The Titanic EDA revealed that survival chances were influenced by gender, passenger class, fare, and age. Females and first-class passengers had significantly better survival rates, suggesting socio-economic status and gender norms impacted rescue priorities.  

---
