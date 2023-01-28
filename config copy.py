import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    APP_USER_ADMIN = str(os.environ.get('APP_USER_ADMIN') ) or 123
    APP_USER_EMAIL = str(os.environ.get('APP_USER_EMAIL') ) or 123
    APP_PASS       = str(os.environ.get('APP_PASS') ) or 123

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


class DevelopmentConfig(Config):
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡')
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡')
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡')
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡')
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡')
    # MongoDB
    MONGODB_HOST          = str(os.environ.get('DEV_MONGODB_HOST'))
    MONGODB_LOCAL_PORT    = int(os.environ.get('DEV_MONGODB_LOCAL_PORT'))
    MONGODB_EXTERNAL_PORT = int(os.environ.get('DEV_MONGODB_EXTERNAL_PORT'))
    MONGODB_USERNAME      = str(os.environ.get('DEV_MONGODB_USERNAME'))
    MONGODB_PASSWORD      = str(os.environ.get('DEV_MONGODB_PASSWORD'))
    MONGODB_TIMEOUT       = int(os.environ.get('DEV_MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST   = bool(os.environ.get('DEV_MONGODB_AUTOREQUEST'))
    DEBUG                 = True


class TestingConfig(Config):
    # MongoDB
    print('TEST 🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    print('🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    print('🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    print('🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    print('🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    print('🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠')
    MONGODB_HOST        = str(os.environ.get('TEST_MONGODB_HOST'))
    MONGODB_PORT        = int(os.environ.get('TEST_MONGODB_LOCAL_PORT'))
    MONGODB_USERNAME    = str(os.environ.get('TEST_MONGODB_USERNAME'))
    MONGODB_PASSWORD    = str(os.environ.get('TEST_MONGODB_PASSWORD'))
    MONGODB_TIMEOUT     = int(os.environ.get('TEST_MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST = bool(os.environ.get('TEST_MONGODB_AUTOREQUEST'))
    DEBUG               = True


class ProductionConfig(Config):
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    print('🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢')    
    # MongoDB
    MONGODB_HOST          = str(os.environ.get('MONGODB_HOST'))
    MONGODB_LOCAL_PORT    = int(os.environ.get('MONGODB_LOCAL_PORT'))
    MONGODB_EXTERNAL_PORT = int(os.environ.get('MONGODB_EXTERNAL_PORT'))
    MONGODB_USERNAME      = str(os.environ.get('MONGODB_USERNAME'))
    MONGODB_PASSWORD      = str(os.environ.get('MONGODB_PASSWORD'))
    MONGODB_TIMEOUT       = int(os.environ.get('MONGODB_TIMEOUT'))
    MONGODB_AUTOREQUEST   = bool(os.environ.get('MONGODB_AUTOREQUEST'))

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
