'Example Module'
import logging

logger = logging.getLogger(__name__)


def log_message(message):
    'Log a message'

    logger.debug('Asked to log message: %s', message)
    logger.info('Logging Message in Module: %s', message)
    
