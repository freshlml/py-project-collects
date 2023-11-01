import logging
from logging import config
from logging import handlers
import chapter7_37.sub
import chapter7_37_1


config.fileConfig("log_config")
logger = logging.getLogger('simpleExample')
print(logger)                             # <Logger simpleExample (DEBUG)>
print(logger is chapter7_37_1.logger)     # True
logger.debug("chapter7_37运行")
chapter7_37_1.md()
chapter7_37.sub.md()
