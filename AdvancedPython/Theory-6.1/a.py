import subprocess
import schedule
import logging
import threading

#logging
logging.basicConfig(filename='backup_cleanup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define source and backup directories and days to keep files
source_directory = '/Users/om-college/Desktop/College/AdvancedPython/Theory-6.1'
backup_directory = '/Users/om-college/Desktop/College/AdvancedPython/backup2'
days_to_keep = 30

# Backup function
def perform_backup():
    try:
        subprocess.run(['rsync', '-av', source_directory, backup_directory])
        logging.info("Backup completed successfully")
    except Exception as e:
        logging.error(f"Backup failed: {str(e)}")

# cleaning function
def perform_cleanup():
    try:
        subprocess.run(['find', source_directory, '-type', 'f', '-mtime', f'+{days_to_keep}', '-delete'])
        logging.info("Cleanup completed successfully")
    except Exception as e:
        logging.error(f"Cleanup failed: {str(e)}")

# Scheduling the backup and cleanup
schedule.every().day.at("18:45:30").do(perform_backup)
schedule.every().day.at("18:45:30").do(perform_cleanup)

# Threading for concurrent execution
backup_thread = threading.Thread(target=perform_backup)
cleanup_thread = threading.Thread(target=perform_cleanup)

backup_thread.start()
cleanup_thread.start()

backup_thread.join()
cleanup_thread.join()

# Main loop for scheduled tasks
while True:
    schedule.run_pending()
