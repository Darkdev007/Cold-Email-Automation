import logging
import os
from datetime import datetime
from pathlib import Path


def get_project_logger(name):
    """
    Initializes and configures a dual-output logger for the project.

    This function sets up a centralized logging mechanism that outputs messages 
    to both the console and a timestamped log file. It ensures that logs are 
    versioned by run time and prevents handler duplication if the logger is 
    called multiple times across different modules.

    Args:
        name: The name of the logger, typically passed as __name__ from 
              the calling module to trace the source of log messages.

    Returns:
        logging.Logger: A configured logger instance with INFO level 
                        setting, StreamHandler, and FileHandler.

    Notes:
        The function creates a '../logs/' directory if it does not exist 
        and generates filenames following the 'run_YYYYMMDD_HHMM.log' pattern.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Use project root for log folder
        PROJECT_ROOT = Path(__file__).resolve().parent.parent  # adjust if needed
        logs_dir = PROJECT_ROOT / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        log_file = logs_dir / f"run_{timestamp}.log"

        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        logger.addHandler(sh)

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger


def return_data_path():
    current_file = os.path.abspath(__file__)
    current_dir  = os.path.dirname(current_file)
    PROJECT_ROOT = os.path.dirname(current_dir)
    EMAIL_PATH = os.path.join(PROJECT_ROOT, "emails.json")
    return EMAIL_PATH