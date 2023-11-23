# Import the NumPy library, which provides useful functions for numerical operations.
import numpy as np

# Scenario: Imagine you work for a manufacturing company, 
# and you need to analyze the quality control data of a production line.
# You have recorded the measurements of the length of 1000 produced widgets.

# Generate a random array of widget lengths (simulating real-world data)
# Here, we use 'np.random.normal' to create a list of 1000 widget lengths.
# 'np.random.normal' generates random numbers that follow a normal distribution.
# The '10' represents the mean (average) length, 
# '1' represents the standard deviation (a measure of variability),
# and '1000' is the number of data points we want to generate.
widget_lengths = np.random.normal(10, 1, 1000) # Create a list of 1000 widget lengths
print(widget_lengths)

# Calculate basic statistics using NumPy

# Calculate the mean (average) length of the widgets.
mean_length = np.mean(widget_lengths)

# Calculate the median length, which is the middle value when all lengths are sorted.
median_length = np.median(widget_lengths)

# Calculate the standard deviation, which measures the spread or variability of the lengths.
std_deviation = np.std(widget_lengths)

# Find the maximum length in the dataset.
max_length = np.max(widget_lengths)

# Find the minimum length in the dataset.
min_length = np.min(widget_lengths)

# Print the results

# Display a header to indicate that we are printing statistics for widget lengths.
print("Statistics for Widget Lengths:")

# Print the mean length with two decimal places.
print(f"Mean Length: {mean_length:.2f} units")

# Print the median length with two decimal places.
print(f"Median Length: {median_length:.2f} units")

# Print the standard deviation with two decimal places.
print(f"Standard Deviation: {std_deviation:.2f} units")

# Print the maximum length with two decimal places.
print(f"Maximum Length: {max_length:.2f} units")

# Print the minimum length with two decimal places.
print(f"Minimum Length: {min_length:.2f} units")
