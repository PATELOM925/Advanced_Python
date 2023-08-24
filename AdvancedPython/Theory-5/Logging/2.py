"""
Aim: Logging with Exception Handling
"""
import logging

# Configure logging by changing level=logging.____  e.g.logging.ERROR
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("Division by zero error")
    else:
        logging.info(f"The result is: {result}")

# Perform division
divide(10, 2)
divide(10, 0)

# Output:
# 2023-08-09 10:00:00,000 - INFO - The result is: 5.0
# 2023-08-09 10:00:00,000 - ERROR - Division by zero error