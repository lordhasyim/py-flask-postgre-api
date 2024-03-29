#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt
# import user_api bluepring
from .views.UserView import user_api as user_blueprint


def create_app(env_name):
    """
    Create App
    """

    #app initialization
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    bcrypt.init_app(app)
    db.init_app(app)
    
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'this is first endpoint'
        
    return app