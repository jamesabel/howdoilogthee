
from howdoilogthee import init_logger

from example import logger, __application_name__

init_logger('log', __application_name__, True, True)
logger.log.info('it worked!')
