from flask.ext.script import Manager, Server
import main


manager = Manager(main.app)


manager.add_command('runserver', Server())


@manager.shell
def make_shell_context():
    """
    create a python CLI.
    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app)


if __name__ == '__main__':
    manager.run()
