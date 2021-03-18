from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Blog, Comment
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment

app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
moment = Moment(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Blog=Blog, Comment=Comment)


manager.add_command('server', Server)


@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)


if __name__ == '__main__':
    manager.run()
