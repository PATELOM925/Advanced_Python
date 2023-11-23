import subprocess
import pandas as pd
import numpy as np
import os
import schedule
import time
import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to read the dataset
def read_dataset():
    try:
        logging.info("Checking if 'students_scores_test.csv' file exists...")
        if not os.path.exists('students_scores_test.csv'):
            logging.error("CSV file is not found.")
            return None
        df = pd.read_csv('students_scores_test.csv')
        logging.info("Dataset read successfully.")
        return df
    except Exception as e:
        logging.error(f"An error occurred while reading the dataset: {str(e)}")
        return None

# Function to display rows 3 to 7
def display_rows(df):
    if df is not None:
        print(df.iloc[2:7])

# Function to find the highest and lowest scores using NumPy and visualize the data
def find_highest_lowest_scores(df):
    if df is not None:
        try:
            highest_score = np.max(df['Score'])
            lowest_score = np.min(df['Score'])
            logging.info(f"Highest Score: {highest_score}, Lowest Score: {lowest_score}")

            # Visualize the scores using Matplotlib and Seaborn
            plt.figure(figsize=(10, 6))
            sns.histplot(df['Score'], bins=20, kde=True)
            plt.xlabel('Scores')
            plt.ylabel('Frequency')
            plt.title('Score Distribution')
            plt.show()

        except Exception as e:
            logging.error(f"An error occurred while calculating highest and lowest scores: {str(e)}")

# Function to filter and save the updated dataset
def filter_and_save_dataset(df):
    if df is not None:
        try:
            filtered_df = df[(df['Score'] > 70) & (df['Group'] == 'A')]
            filtered_df.to_csv('updated_data.csv', index=False)
            logging.info("Saving the updated dataset to 'updated_data.csv'.")
        except Exception as e:
            logging.error(f"An error occurred while filtering and saving the dataset: {str(e)}")

# Schedule the task to run on the 1st date of every month at 00:00 AM
schedule.every().month.at('00:00').do(lambda: run_task())

# Function to run the entire task
def run_task():
    logging.info("Task started.")
    df = read_dataset()
    if df is not None:
        display_rows(df)
        find_highest_lowest_scores(df)
        filter_and_save_dataset(df)
    logging.info("Task completed.")
    logging.shutdown()

while True:
    schedule.run_pending()
    time.sleep(1)
