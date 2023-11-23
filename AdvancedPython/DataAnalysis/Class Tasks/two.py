import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # for complex statistical plots

# Load your dataset
# Replace 'two_dataset.csv' with your data file
data = pd.read_csv('two_dataset.csv') # dataframe 'data'

# Data Cleaning and Preprocessing
# You can perform various cleaning and preprocessing steps here
# For example, removing missing values
data = data.dropna() 

# Data Visualization
# You can customize the visualizations based on your dataset and requirements

# Example 1: Pair Plot using Seaborn
sns.pairplot(data, hue='target_variable', diag_kind='kde')
# The 'hue' parameter specifies a categorical variable, and it will color the data points in the pair plot based on the values of this variable.
# The 'diag_kind' parameter specifies what to display on the diagonal of the pair plot. Setting it to 'kde' means that it will display kernel density estimates, which can give you a sense of the data's distribution for each variable.
plt.title('Pair Plot')
plt.show()

# Example 2: Histogram
plt.hist(data['feature'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Feature')
plt.ylabel('Count')
plt.title('Histogram')
plt.show()

# Example 3: Box Plot
sns.boxplot(x='category', y='value', data=data)
plt.title('Box Plot')
plt.show() # The box shows the interquartile range (IQR) with the median marked as a line inside

# Example 4: Correlation Heatmap
# Exclude the non-numeric columns
numeric_data = data.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_data.corr() #computes the correlation matrix of your dataset, assuming that you have a DataFrame named data containing numerical data
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Example 5: Bar Plot
sns.barplot(x='category', y='value', data=data)
plt.title('Bar Plot')
plt.show()
# Lines Extending from the Box represent errors

# Example 6: Scatter Plot
plt.scatter(data['x'], data['y'], c=data['target_variable'], cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()
#cmap='viridis': This argument specifies the color map to be used for coloring the data points. 'Viridis' is one of the available color maps in matplotlib, and it is a perceptually uniform colormap that varies from yellow to blue, with green in between

data = data[(data['column'] >= 10) & (data['column'] <= 100)]
# Example 7: Violin Plot combines a box plot with a kernel density plot, showing the distribution of data across different categories or groups.
sns.violinplot(x='category', y='value', data=data)
plt.title('Violin Plot')
plt.show()

# Example 8: Count Plot (like a bar plot) is a way to show the counts of observations in each category of a categorical variable.
sns.countplot(x='category', data=data)
plt.title('Count Plot')
plt.show()

# Example 9: Time Series Plot displays data points collected or recorded over a continuous time interval. 
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
data['value'].plot()
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Example 10: Stacked Bar Plot to represent the composition of a whole (a total) broken down into different categories or components.
pivot_table = data.pivot_table(index='category', columns='subcategory', values='value', aggfunc='sum')
pivot_table.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Plot')
plt.show()
# pivot_table: This line of code creates a pivot table using the pivot_table function in pandas. The pivot table is formed from the original 'data' DataFrame and is used to reshape the data for visualization.
# index='category': This specifies the variable to be used as the index (x-axis in the resulting plot). In this case, it's 'category,' which will be represented on the x-axis.
# columns='subcategory': This specifies the variable to be used for creating different columns (different bars) in the plot. Each unique 'subcategory' will become a separate column in the resulting plot.
# values='value': This specifies the variable that holds the values that will be aggregated. The values in the 'value' column will be used to fill the cells of the pivot table.
# aggfunc='sum': This specifies the aggregation function to be used when combining data for the same 'category' and 'subcategory' combination. In this case, it's 'sum,' so the values are summed up.
# pivot_table.plot(kind='bar', stacked=True): This line of code creates a stacked bar plot from the pivot table.
# kind='bar': This parameter specifies the type of plot, which is a bar plot in this case.
# stacked=True: This parameter makes the bars in the plot stacked on top of each other.

# Example 11: PairGrid with Custom Scatter Plots to differentiate data points by a specific target variable
g = sns.PairGrid(data, hue='target_variable')
g.map(plt.scatter) # A scatter plot will be created for each combination of variables in the dataset. 
g.add_legend() # Adds a legend to understand which colors correspond to which values of the 'target_variable'.
plt.suptitle('PairGrid with Custom Scatter Plots') #sets the super title of the entire PairGrid plot, providing an overall title for the visualization
plt.show()

# Example 12: Heatmap of Missing Data
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Data')
plt.show()
# cbar=False argument removes the color bar
# cmap='viridis' argument sets the color map to "viridis." 
# Cells with missing data will be shown in one color (as specified by the 'viridis' colormap), while cells with False values (non-missing data) will be shown in another color