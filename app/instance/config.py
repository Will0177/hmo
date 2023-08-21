# instance/config.py

import os

class Config:
    # Set your secret key for sessions and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

    # SQLite database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'database.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Create an instance of the Config class to be used as app_config
app_config = Config()