"""Custom Logger for the application"""
import logging
import os
from functools import lru_cache
from rich.logging import RichHandler
from rich.traceback import install
from rich.console import Console
from pathlib import Path
from backend.core.path_config import LOGPATH
from backend.core.config import settings



class BetrLogger:
    """Custom Logging implementation for the application utilizing the Rich library.

    Attributes:
        logger (logging.Logger): The logger instance for the application.
        log_file (str): The path to the log file for the application.
        log_error_file (str): The path to the error log file for the application.

    Methods:
        setup_logger(): Set up the logger for the application.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.log_err_file = settings.LOG_STDERR_FILENAME
        self.log_std_out_file = settings.LOG_STDOUT_FILENAME

    def setup_logger(self):
        """Set up the logger for the application."""
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler = logging.FileHandler(self.log_std_out_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        error_file_handler = logging.FileHandler(self.log_err_file)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)
        console_handler = RichHandler(show_path=False)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(error_file_handler)
        self.logger.addHandler(console_handler)
        return self.logger
    
    def log(self, message: str, level: str = "info"):
        """Log a message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    
    
    def log_traceback(self, message: str, level: str = "error"):
        """Log a traceback to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message, exc_info=True)
        elif level == "warning":
            self.logger.warning(message, exc_info=True)
        elif level == "error":
            self.logger.error(message, exc_info=True)
        elif level == "critical":
            self.logger.critical(message, exc_info=True)
        else:
            self.logger.debug(message, exc_info=True)
        return self.logger
    
    def log_critical(self, message: str, level: str = "critical"):
        """Log a critical message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    
    def log_debug(self, message: str, level: str = "debug"):
        """Log a debug message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    
    def log_info(self, message: str, level: str = "info"):
        """Log an info message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    
    def log_warning(self, message: str, level: str = "warning"):
        """Log a warning message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    
    def log_error(self, message: str, level: str = "error"):
        """Log an error message to the application log file.

        Args:
            message (str): The message to log.
            level (str): The level at which to log the message.
        """
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.debug(message)
        return self.logger
    


if __name__ == "__main__":
    logger = BetrLogger()
    logger.setup_logger()
    logger.log("This is a test message", "info")
    logger.log_critical("This is a test message", "critical")
    logger.log_debug("This is a test message", "debug")
    logger.log_info("This is a test message", "info")
    logger.log_warning("This is a test message", "warning")
    logger.log_error("This is a test message", "error")



