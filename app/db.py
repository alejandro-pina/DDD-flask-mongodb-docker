from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
class DB:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        else:
            self.db = None

    def init_app(self, app):
        mode     = app.config['MODE']
        host     = app.config['MONGODB_HOST']
        port     = app.config['MONGODB_EXTERNAL_PORT']
        if mode != 'prod':
            port     = app.config['MONGODB_LOCAL_PORT']
        username = app.config['MONGODB_USERNAME']
        password = app.config['MONGODB_PASSWORD']
        timeout  = app.config['MONGODB_TIMEOUT']
        print('\033[93m 🟡🟡🟡 Connecting to database...')
        print('===>',mode,
        host     ,
        port     ,
        username ,
        password ,
        timeout  )
        try:
            self.db = MongoClient(
                host                     = host,
                port                     = port,
                username                 = username,
                password                 = password,
                serverSelectionTimeoutMS = timeout
            )
            self.db.server_info()
            print('\033[92m 🟢🟢🟢 Connected to the MongoDB Server!')
        except OperationFailure:
            raise ValueError('🔴🔴🔴 Database not found.')
        except ServerSelectionTimeoutError:
            raise ValueError('🔴🔴🔴 MongoDB Server is down.')


    def __getattr__(self, name):
        if name == 'database':
            if self.database is None:
                raise ValueError("Database not initialized. Make sure to call `init_app` before using the `database` attribute.")
            return self.database
        return getattr(self.db, name, None)