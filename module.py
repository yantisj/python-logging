'Example Module'
import logging

logger = logging.getLogger(__name__)


def say_something(something):
    'Say something'

    logger.debug('Asked to say something: %s', something)
    logger.warning('Warning Module Test')

    print(something)
    
