"""
Aim: Basics of Logging

Functions included:
--> debug()
--> info()
--> warning()
--> error()
--> critical()
"""
#'logging' module provides a flexible and configurable way to record status, error, and informational 
# messages during the execution of a program. It's an essential tool for monitoring and debugging 
# applications. 
import logging
# Configure the root logger
logging.basicConfig(level=logging.INFO)

# Create a logger for a specific module; All loggers are descendants of the root logger
logger = logging.getLogger('my_module') #"my_module" can be any Python module which is source of log messages

# Create a file handler
file_handler = logging.FileHandler('my_module.log')

# Create a console handler (you can use file or console handler or both-as in this case)
console_handler = logging.StreamHandler()

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Attach the formatter to the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler) # IF YOU COMMENT THIS LINE, LOG messages won't be displayed in the console

# Log messages at different levels
logger.debug('This is a debug message') # won't be displayed as logging level is INFO
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

""" 
DEBUG: Detailed debugging information, typically useful only during development or troubleshooting. 
INFO: General information about the program's execution process. 
      This is usually used to confirm that things are working as expected. 
WARNING: Indications of potentially harmful situations or unexpected behavior. 
      The program can continue to run. 
ERROR: Errors that prevent the program from performing a specific function or operation. 
      The program can still continue in most cases. 
CRITICAL: Critical errors that might lead to application failure. 
      The program might not be able to continue running after such an error. 

# Output:
# 2023-08-09 10:00:00,000 - WARNING - This is a warning message
# 2023-08-09 10:00:00,000 - ERROR - This is an error message
# 2023-08-09 10:00:00,000 - CRITICAL - This is a critical message
"""