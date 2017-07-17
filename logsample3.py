#!/usr/bin/env python3
import logging
import argparse
import configparser
import requests
import module

DEBUG = 0
CONFIG_FILE = 'logsample.ini'

logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

def init_logging():
    'Initialize Logging Globally'

    log_level = int(config['main']['log_level'])

    if DEBUG:
        log_level = logging.DEBUG

    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    root_logger = logging.getLogger()

    # Set root logger to debug always
    root_logger.setLevel(logging.DEBUG)

    # File Handler
    fh = logging.FileHandler('example.log')

    # Always log at INFO or below
    if log_level < logging.INFO:
        fh.setLevel(log_level)
    else:
        fh.setLevel(logging.INFO)

    fh.setFormatter(log_format)
    root_logger.addHandler(fh)

    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(log_format)
    root_logger.addHandler(ch)

init_logging()

# Set urllib3 logging to WARNING
#logging.getLogger('urllib3').setLevel(logging.WARNING)


url = 'https://www.google.com'
logger.debug('Requesting URL: %s', url)
r = requests.get(url)

if r.status_code == 200:
    logger.info('Successfully retrieved URL: %s', url)
print(str(r.status_code))
logger.debug('First 50 chars returned from URL: %s', r.text[:50])

module.say_something('Testing')

logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')

try:
    1/0
except Exception as e:
    #logger.error(e, exc_info=True)
    logger.error(e)
    #logger.exception('Divide by 0')
