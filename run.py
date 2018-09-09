import os
from application.__init__ import createApp
from flask_script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand

app = createApp(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
if __name__ == '__main__':
    manager.run()