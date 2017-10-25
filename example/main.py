
from howdoilogthee import init_logger

from example import logger, __application_name__, do_something

init_logger('log', __application_name__, True, True)
logger.log.info('I can log!')
do_something.do_something()
