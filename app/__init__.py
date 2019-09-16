import os

from flask import Flask
from . import fibo

def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(fibo.bp)

    return app
