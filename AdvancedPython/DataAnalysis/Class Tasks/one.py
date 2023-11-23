# Import necessary libraries
import numpy as np
import pandas as pd

# Load data from 'combined_arrays.csv'
df_numpy = pd.read_csv("combined_arrays.csv", header=None)
print("Data frame",df_numpy)
# Calculate the mean of the DataFrame
for_mean = df_numpy.mean()
print("Mean Result:")
print(for_mean)

# Calculate the median of the DataFrame
for_median = df_numpy.median()
print("median Result:")
print(for_median)
# Calculate the standard deviation of the DataFrame
for_std = df_numpy.std()
print("std Result:")
print(for_std)

# Calculate the mode of the DataFrame
for_mode = df_numpy.mode()
print("mode Result:")
print(for_mode)

# Reload the data from 'combined_arrays.csv' with header=None
# reloaded_data = pd.read_csv('combined_arrays.csv')

# Split the reloaded data into two variables, var1 and var2
var1 = df_numpy.iloc[:-1].values  # Select all rows in the DataFrame except the last row
var2 = df_numpy.iloc[-1].values # Select the last row
# iloc is used to select rows and columns by their integer position

print(var1)
print(var2)
# Calculate the dot product of var1 and var2
result = np.dot(var1, var2)

# Print the result of the dot product
print("Dot Product Result:")
print(result)

# Load data from 'test2.csv'
another_csv = pd.read_csv("test2.csv")

# Display the first 2 rows of the DataFrame
print(another_csv.head(2))

# Display the last 2 rows of the DataFrame
print(another_csv.tail(2))

# Count the number of missing values in each column
print(another_csv.isnull().sum())

# Fill missing values with 0 in 'Identifier' (other methods can be used for filling)
another_csv['Identifier'].fillna(value=0, method=None, axis=None, inplace=True, limit=None, downcast=None)

another_csv['First Given Name'].fillna(value='Unknown', inplace=True)
# value: specify the value to be filled
# method: If you set method to a value other than None, you can choose a method for filling in missing values. For example, you can use methods like 'ffill' (forward fill) to fill missing values with the previous non-missing value, or 'bfill'
# inplace: When set to True, will modify the DataFrame in place, and it won't return a new DataFrame.
# limit: If you want to limit the number of replacements, you can specify an integer value here.
# downcast: It's used to specify the data type to which you want to downcast the resulting DataFrame. For example, you can downcast to 'integer' data type if needed. This may help reduce memory by converting it to a smaller integer type

# Save the DataFrame with filled missing values to a new CSV file 'filling_null.csv'
another_csv.to_csv("filling_null.csv")

# Count the number of missing values in each column after filling
print(another_csv.isnull().sum())

# Display summary statistics of the DataFrame
print(another_csv.describe())

# Import Matplotlib for data visualization
import matplotlib.pyplot as plt

# Convert date columns to datetime objects (if needed)
another_csv['Start Date of Subscription'] = pd.to_datetime(another_csv['Start Date of Subscription'], format='%d-%m-%Y')
another_csv['End Date of Subscription'] = pd.to_datetime(another_csv['End Date of Subscription'], format='%d-%m-%Y')

# Create a line chart for "Total Amount Spent" over time
plt.figure(figsize=(12, 6)) # set the size of the figure to 12 inches in width and 6 inches in height.
plt.plot(another_csv['Start Date of Subscription'], another_csv['Total Amount Spent'], marker='o', linestyle='-')
# Creates a line plot with markers ('o') and ('-'). Use 'Start Date of Subscription' for the x-axis and 'Total Amount Spent' for the y-axis.
plt.title('Total Amount Spent Over Time') #  Set the title of the plot.
plt.xlabel('Start Date of Subscription')
plt.ylabel('Total Amount Spent')
plt.grid(True)
plt.xticks(rotation=45) # Rotate the x-axis labels by 45 degrees for better readability.
plt.tight_layout() # Ensure that the plot elements do not overlap and that the plot looks well-organized 
plt.show() # Display the line chart

# Create a histogram for the "Total Amount Spent" column
plt.figure(figsize=(8, 6))
plt.hist(another_csv['Total Amount Spent'], bins=20, color='skyblue', edgecolor='black')
#  takes the 'Total Amount Spent' column, specifies 20 bins for the histogram, fill color to 'skyblue', and the edge color of the bars to 'black'
plt.title('Histogram of Total Amount Spent')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency')
plt.grid(True)
plt.show() # Display the histogram

# Count the number of members for each level
member_level_counts = another_csv['Member Level'].value_counts()
print(member_level_counts)
# Create a pie chart for the "Member Level" column
plt.figure(figsize=(8, 8))
plt.pie(member_level_counts, labels=member_level_counts.index, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribution of Member Levels')
plt.axis('equal') # Ensure that the aspect ratio of the pie chart is equal, so it appears as a circle rather than an ellipse.
plt.show() # Display the pie chart
#member_level_counts: This is a data array that contains the values for each slice of the pie chart.
#labels=member_level_counts.index: Assigns labels to each slice of the pie chart, taken from the index of the member_level_counts series.
#autopct='%1.1f%%': It displays the percentage for each slice with one decimal place.
#startangle=140: Specifies the angle at which the first slice of the pie chart begins. In this case, it starts at 140 degrees (measured counterclockwise from the positive x-axis).
#colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen']: This sets the colors for each slice of the pie chart.
# Convert date columns to datetime objects (if needed)

another_csv['Start Date of Subscription'] = pd.to_datetime(another_csv['Start Date of Subscription'], format='%d-%m-%Y')
# Sort the DataFrame by the start date
another_csv.sort_values(by='Start Date of Subscription', inplace=True)

# Create a filled area plot for "Total Amount Spent" over time
plt.figure(figsize=(12, 6))
plt.fill_between(another_csv['Start Date of Subscription'], another_csv['Total Amount Spent'], color='lightblue', alpha=0.7)
# another_csv['Start Date of Subscription']: Specifies the x-values
# another_csv['Total Amount Spent']:Specifies the y-values
# color='lightblue': Sets the color of the filled area to light blue.
# alpha=0.7: Controls the transparency of the filled area. 
plt.title('Area Plot of Total Amount Spent Over Time')
plt.xlabel('Start Date of Subscription')
plt.ylabel('Total Amount Spent')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() # Display the area plot

# Convert date columns to datetime objects (if needed)
another_csv['Birthdate'] = pd.to_datetime(another_csv['Birthdate'], format='%d-%m-%Y')
# Create a scatter plot for "Total Amount Spent" vs. "Age/Birthdate"
plt.figure(figsize=(10, 6))
plt.scatter(another_csv['Birthdate'], another_csv['Total Amount Spent'], c='blue', marker='o', alpha=0.7)
plt.title('Scatter Plot of Total Amount Spent vs. Birthdate')
plt.xlabel('Birthdate')
plt.ylabel('Total Amount Spent')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() # Display the scatter plot
