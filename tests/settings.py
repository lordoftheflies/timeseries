import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'tdzf@9g8lofi@lo$=126jrka1ydzjix^!8j)vg$6cd+kz^ei5h'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'tests'
]

DEBUG = True

test_db = os.environ.get('TEST_DB_CONFIG', 'test')
db_user = os.environ.get('TEST_DB_USER', os.environ.get('USER', 'django'))
db_name = 'timerseries_tests' + os.environ.get('TEST_DB_NAME', 'test')

DB_CONFIGS = {
    # N.B. sqlite doesn't support DISTINCT ON for some reason... ???
    'test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'test',
        'USER': 'django',
        'PASSWORD': 'qwe123'
    }
}

DATABASES = {
    'default': DB_CONFIGS.get(test_db)
}
