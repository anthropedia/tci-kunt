import os
from pathlib import Path


DEBUG = os.environ.get('DEBUG', False)
PORT = int(os.environ.get('PORT', 5000))
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(16))

DATABASE = {'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')}

# Skip authentication. Useful for testing and offline.
AUTH_DISABLED = os.environ.get('AUTH_DISABLED', False)

TCIAPI_URL = os.environ.get('TCIAPI_URL', 'http://localhost:5001')
TCIAPI_TOKEN = os.environ.get('TCIAPI_TOKEN')

ROOT_PATH = Path(__file__).parent

TRANSLATION_CACHE = os.environ.get('TRANSLATION_CACHE', True)
TRANSLATION_FILES = {
    'en': ROOT_PATH / 'trans.en.csv',
}
