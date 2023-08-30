import schedule
import shutil
import time
import datetime
import webbrowser

def backup_daily(source_dir,backup_dir):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    backup_folder = f'{backup_dir}/backup_{timestamp}' #giving our backup_dir a name as backup_folder
    
    try:
        shutil.copytree(source_dir,backup_folder) #copies all the files/flder from source directory to our backup folder
        print(f'Backup Created at {backup_folder}')
    except Exception as e:
        print("Error",e) 
        
def openTeams():
    webbrowser.open("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:6NgJRESII60bghLZ31Irpb54ZXOptflo4X2OXL0IfUE1@thread.tacv2&ctx=channel",new=2)
    print("Microsoft Teams Has been Opened")
        
if __name__ == "__main__":
    
    source_dir = "/Users/om-college/Desktop/College/AdvancedPython/Theory-6"
    backup_dir = "/Users/om-college/Desktop/College/AdvancedPython/backup"
    
    schedule.every().monday.at('10:06:55').do(openTeams)
    schedule.every().day.at('10:05:55').do(backup_daily,source_dir,backup_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)
   

