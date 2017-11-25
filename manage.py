from flask_script import Manager, Server
import main
import models


manager = Manager(main.app)


manager.add_command('runserver', Server())


@manager.shell
def make_shell_context():
    """
    create a python CLI.
    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app,
                db=models.db,
                User=models.User)


if __name__ == '__main__':
    manager.run()
