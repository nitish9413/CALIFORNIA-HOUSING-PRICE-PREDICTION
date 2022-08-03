from fileinput import filename
import logging
from datetime import datetime
import os
from stat import filemode

LOG_DIR="housing_logs"

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%y-%m-%d_%H-%M-%S')}"

LOF_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR)

LOG_FILE_PATH=os.path.join(filename=LOG_FILE_PATH,
filemode='w',
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)