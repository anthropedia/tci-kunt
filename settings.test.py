import os


PORT = int(os.environ.get('PORT', 5000))
DEBUG = True
SECRET_KEY = 'my secret key'

# MongoDB
DATABASE = {
  'db': 'tci_test',
  'username': '',
  'password': '',
  'host': 'localhost',
  'port': 27017,
}

TRANSLATION_FILES = {
    'fr': '/Users/vinyll/Projects/tci-online/fr.csv',
    'sv': '/Users/vinyll/Projects/tci-online/se.csv',
    'en': '/Users/vinyll/Projects/tci-online/en.csv',
}
