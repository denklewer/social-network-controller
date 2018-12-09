import os
import logging

__logger = logging.getLogger("config_parser")

# parsing SCVMM config
MONGODB_URL = "mongodb://%s:%s@35.204.169.59:27017/"
if "MONGODB_URL" in os.environ:
    MONGODB_URL = os.environ['MONGODB_URL']

# parsing logging level
LOGGING_LEVEL = logging.INFO
__levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}
if "LOG_LEVEL" in os.environ and os.environ['LOG_LEVEL'] in __levels:
    LOGGING_LEVEL = __levels[os.environ['LOG_LEVEL']]

# parsing cookies config
COOKIE_EXPIRE_TIME_HOURS = 6
if "COOKIE_EXPIRE_TIME_HOURS" in os.environ:
    try:
        COOKIE_EXPIRE_TIME_HOURS = int(os.environ['COOKIE_EXPIRE_TIME_HOURS'])
    except (ValueError, TypeError):
        __logger.exception("Value of COOKIE_EXPIRE_TIME_HOURS is erroneous.")

COOKIE_CLEAN_TIMER_MINUTES = 20
if "COOKIE_CLEAN_TIMER_MINUTES" in os.environ:
    try:
        COOKIE_CLEAN_TIMER_MINUTES = int(os.environ['COOKIE_CLEAN_TIMER_MINUTES'])
    except (TypeError, ValueError):
        __logger.exception("Value of COOKIE_CLEAN_TIMER_MINUTES is erroneous.")
