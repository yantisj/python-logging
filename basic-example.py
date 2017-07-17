#!/usr/bin/env python3
import logging
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
                    level=logging.DEBUG)

logging.debug('Debug Message')
logging.info('Info Message')
logging.warning('Warning Message')

# Silence urllib3 debug
logging.getLogger('urllib3').setLevel(logging.WARNING)

url = 'https://www.google.com/'

try:
    r = requests.get(url)

    if r.status_code == 200:
        logging.info('Successfully retrieved URL: %s', url)
    else:
        logging.critical('Failed to retrieve url: %s Status: %s', url, str(r.status_code))
except Exception as e:
    logging.error(e)
    #logging.error(e, exc_info=True)
