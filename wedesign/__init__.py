from flask import Flask
from .routes import bp

def create_app(
        package_name=__name__, 
        static_folder='static',
        template_folder='templates',
        **config_overrides):

    # initialize app
    app = Flask(package_name,
                static_url_path='/assets',
                static_folder=static_folder,
                template_folder=template_folder)

    # Apply overrides
    app.config.update(config_overrides)

    # Register Routes in routes.py
    app.register_blueprint(bp)

    return app

