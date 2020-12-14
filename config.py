class Config(object):
  DEBUG = False
  TESTING = False

  db_username = 'b186c5c37cabe7'
  db_password = 'e0a20b6f'
  db_host = 'us-cdbr-east-02.cleardb.com'
  db_db = 'heroku_692a2fabb989b2a'

  SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_db)

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True

