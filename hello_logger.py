import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create and configure logger
logging.basicConfig(filename = "file.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT
                    ,#filemode = 'w' # append is the default filemode, w overwrite
                    )
logger = logging.getLogger()

# test the logger
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

print(logger.level)