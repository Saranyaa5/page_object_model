# import logging
# import inspect

# def get_logger():
 
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
 
#         filehandler = logging.FileHandler('logfile.log')
 
#         formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#         filehandler.setFormatter(formatter)
 
#         logger.addHandler(filehandler)  
 
#         logger.setLevel(logging.INFO)
#         return logger
# import logging
# import inspect

# def get_logger():
 
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
 
#         filehandler = logging.FileHandler('logfile.log')
 
#         formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#         filehandler.setFormatter(formatter)
 
#         logger.addHandler(filehandler)  
 
#         logger.setLevel(logging.INFO)
#         return logger

import logging
import inspect

def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # Avoid adding multiple handlers if logger already has one
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # File Handler
        file_handler = logging.FileHandler('logfile.log')
        file_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(file_formatter)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(levelname)s : %(message)s")
        console_handler.setFormatter(console_formatter)

        # Add both handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
