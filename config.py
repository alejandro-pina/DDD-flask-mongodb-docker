import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    APP_USER_ADMIN = str(os.environ.get('APP_USER_ADMIN') ) or 'alexddd'
    APP_USER_EMAIL = str(os.environ.get('APP_USER_EMAIL') ) or 'alejandropina.com'
    APP_PASS       = str(os.environ.get('APP_PASS') ) or 'alexddd'

    # URL API
    API_PUBLIC = "/api/"

     # URL Auth
    AUTH_PATH = "/auth/"

    # JWT
    JWT_ACCESS_TOKEN_EXPIRES  = eval(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') )
    JWT_SECRET_KEY            = str(os.environ.get('JWT_SECRET_KEY') )

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    MODE                  = 'dev'
    MONGODB_HOST          = str(os.environ.get('DEV_MONGODB_HOST'))
    MONGODB_LOCAL_PORT    = int(os.environ.get('DEV_MONGODB_LOCAL_PORT'))
    MONGODB_EXTERNAL_PORT = int(os.environ.get('DEV_MONGODB_EXTERNAL_PORT'))
    MONGODB_USERNAME      = str(os.environ.get('DEV_MONGODB_USERNAME'))
    MONGODB_PASSWORD      = str(os.environ.get('DEV_MONGODB_PASSWORD'))
    MONGODB_TIMEOUT       = int(os.environ.get('DEV_MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST   = bool(os.environ.get('DEV_MONGODB_AUTOREQUEST'))
    DEBUG                 = True


class TestConfig(Config):
    MODE                  = 'test'
    MONGODB_HOST          = str(os.environ.get('TEST_MONGODB_HOST'))
    MONGODB_LOCAL_PORT    = int(os.environ.get('TEST_MONGODB_LOCAL_PORT'))
    MONGODB_EXTERNAL_PORT = int(os.environ.get('TEST_MONGODB_LOCAL_PORT'))
    MONGODB_USERNAME      = str(os.environ.get('TEST_MONGODB_USERNAME'))
    MONGODB_PASSWORD      = str(os.environ.get('TEST_MONGODB_PASSWORD'))
    MONGODB_TIMEOUT       = int(os.environ.get('TEST_MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST   = bool(os.environ.get('TEST_MONGODB_AUTOREQUEST'))
    DEBUG               = True


class ProdConfig(Config):
    MODE                  = 'prod'
    MONGODB_HOST          = str(os.environ.get('MONGODB_HOST'))
    MONGODB_LOCAL_PORT    = int(os.environ.get('MONGODB_LOCAL_PORT'))
    MONGODB_EXTERNAL_PORT = int(os.environ.get('MONGODB_EXTERNAL_PORT'))
    MONGODB_USERNAME      = str(os.environ.get('MONGODB_USERNAME'))
    MONGODB_PASSWORD      = str(os.environ.get('MONGODB_PASSWORD'))
    MONGODB_TIMEOUT       = int(os.environ.get('MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST   = bool(os.environ.get('MONGODB_AUTOREQUEST'))

config = {
    'development': DevConfig,
    'testing'    : TestConfig,
    'production' : ProdConfig,
    'default'    : DevConfig
}

