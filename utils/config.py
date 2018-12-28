from utils.functions import get_sqlalchemy_uri
from utils.setting import DATABASE


class Conf():
    SQLALCHEMY_DATABASE_URI = get_sqlalchemy_uri(DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SECRET_KEY = 'fkhqjhyr38r1khgjr1h2r4'