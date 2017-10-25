
from howdoilogthee import init_logger

from example import logger

init_logger('log', 'example', True, True)
logger.log.info('it worked!')
