import os

DEBUG = True

VERIFY = False

DEED_API_BASE_HOST = os.getenv('DEED_API_ADDRESS',
                               'http://0.0.0.0:9020')
