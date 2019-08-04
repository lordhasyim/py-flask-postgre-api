import os
from src.app import create_app, db
from src.models import UserModel, BlogpostModel
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# from src.models import UserModel
# from src.models import BlogpostModel

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
