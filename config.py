import os
from dotenv import load_dotenv

load_dotenv()

TEST_ENVIRONMENT = os.environ.get('TEST_ENVIRONMENT')

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

TEST_REDIS_HOST = os.environ.get('TEST_REDIS_HOST')

if TEST_ENVIRONMENT:
    REDIS_HOST = TEST_REDIS_HOST
