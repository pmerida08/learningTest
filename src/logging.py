import logging
from enum import StrEnum

LOG_FORMAT_DEBUG = "%(levelname)s:%(message)s:%(pathname)s:%(funcName)s:%(lineno)d"

class LogLevels(StrEnum):
    info = "INFO"
    debug = "DEBUG"
    warn = "WARN"
    error = "ERROR"
    
def configure_logging(log_level: str = LogLevels.error):
    
    log_level = str(log_level).upper()
    log_levels = [level.value for level in LogLevels]
    
    if log_level not in log_levels:
        logging.basicConfig(
            level=logging.ERROR,
            format=LOG_FORMAT_DEBUG
        )
        return
    
    if log_level == LogLevels.debug:
        logging.basicConfig(
            level=log_level,
            format=LOG_FORMAT_DEBUG
        )
        return
    
    logging.basicConfig(
        level=log_level,
        format="%(levelname)s:%(message)s"
    )
    
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)