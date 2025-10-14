import os
import logging
from datetime import datetime


log_file = f"{datetime.now(). strftime("%m_%d_%Y_%H_%M_%S")}.log"
log_dir = "logs"
log_path = os.path.join(log_dir, log_file)

os.makedirs(log_path, exist_ok=True)

logging.basicConfig(
    filename=log_path
    format="[ %(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)