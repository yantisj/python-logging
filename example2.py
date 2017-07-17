#!/usr/bin/env python3
import logging
import requests



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.debug('Debug Test')
logging.warning('Warning Test')

url = 'https://www.google.com'
r = requests.get(url)

if r.status_code == 200:
    logging.info('Successfully retrieved URL: %s', url)
print(str(r.status_code))

