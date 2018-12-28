
from flask_script import Manager

from utils.app import Create_app

app = Create_app()


manage = Manager(app)
if __name__ == '__main__':
    manage.run()


