from flask import Flask
from config import config

# 创建出app对象
def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from application.views import index
    from application.views import system
    app.register_blueprint(index.mod)
    app.register_blueprint(system.mod)

    return app
