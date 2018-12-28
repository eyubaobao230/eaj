from functools import wraps

from flask import session, url_for
from werkzeug.utils import redirect


def is_login(func):
    @wraps(func)
    def check_status(*args, **kwargs):
        try:
            session['user_id']
        except:
            return redirect(url_for('user.login'))
        return func(*args, **kwargs)
    return check_status



def get_sqlalchemy_uri(DATABASE):
    user = DATABASE['USER']
    password = DATABASE['PASSWORD']
    host = DATABASE['HOST']
    port = DATABASE['PORT']
    name = DATABASE['NAME']
    engine = DATABASE['ENGINE']
    driver = DATABASE['DRIVER']

    return '%s+%s://%s:%s@%s:%s/%s' % (engine, driver, user, password, host, port, name)






