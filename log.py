import logging

LoggingLevel = int

logger = logging.getLogger(__name__)

def log(message: str, handler: str, format: str = "%(asctime)s:%(name)s[%(levelname)s] - %(message)s", level: LoggingLevel = logging.DEBUG) -> None:

    logger.setLevel(level)

    formatter = logging.Formatter(format)

    file_handler = logging.FileHandler(handler)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.log(level, message)

def console_log(message: str, format: str = "%(asctime)s:%(name)s:%(message)s", level: LoggingLevel = logging.DEBUG) -> None:
    
    logger.setLevel(level)

    formatter = logging.Formatter(format)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    logger.log(level, message)