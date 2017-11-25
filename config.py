class Config(object):
    """
    Base config class.
    """
    pass


class ProdConfig(Config):
    """
    Production config class.
    """
    pass


class DevConfig(Config):
    """
    Development config class.
    """
    # open the dubug
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:python@127.0.0.1:3306/flask1'
