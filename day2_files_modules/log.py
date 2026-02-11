import logging
from datetime import datetime

def setup_logger():
    """
    function for setting a logger
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"app_{timestamp}.log"
    logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

    return logging.getLogger()

    
logger = setup_logger()
logger.info("Application started")
logger.info('This is an info message.')

