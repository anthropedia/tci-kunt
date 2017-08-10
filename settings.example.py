import os


PORT = int(os.environ.get('PORT', 5000))

DEBUG = True
SECRET_KEY = ''

# MongoDB
DATABASE = {
  'db': '',
  'username': '',
  'password': '',
  'host': 'localhost',
  'port': 27017,
}

TRANSLATION_FILES = {
    'en': '/path/to/my/transfile.en.csv',
    'fr': '/path/to/my/transfile.fr.csv',
    'sv': '/path/to/my/transfile.sv.csv',
}
