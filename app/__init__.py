from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from instance.config import app_config
from app.instance.config import app_config


database = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=app_config):
    application = Flask(__name__)    
    application.config.from_object(config_class)

    #Initialization of apps
    database.init_app(application)
    migrate.init_app(app=application, 
    db=database, 
    directory="intron_health_migrations",
    render_as_batch=True,
    )

    with application.app_context():

        # Import all BluePrints
        from .home import home as home_blueprint
        application.register_blueprint(home_blueprint, url_prefix="/home")

        return application
