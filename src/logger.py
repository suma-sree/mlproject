import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #name for the file that is being created
logs_path = os.path.join(os.getcwd() , 'logs' , LOG_FILE) #A folder named logs would be created in the cwd andthe log_file would besaved into the folder
os.makedirs(logs_path , exist_ok = True) #even there are files in the folder keep appending new files to it 


LOG_FILE_PATH = os.path.join(logs_path , LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


# if __name__ == "__main__":
#     logging.info("Logging has started")
