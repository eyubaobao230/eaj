from flask import Flask

from app.house_views import h_blue
from app.models import db
from app.order_views import o_blue
from app.user_views import u_blue
from utils.config import Conf
from utils.setting import STATIC_PATH, TEMPLATE_PATH


def Create_app():
    app = Flask(__name__,
                static_folder=STATIC_PATH,
                template_folder=TEMPLATE_PATH)
    # 配置
    app.config.from_object(Conf)
    # 注册蓝图
    app.register_blueprint(blueprint=u_blue,url_prefix='/user')
    app.register_blueprint(blueprint=o_blue,url_prefix='/order')
    app.register_blueprint(blueprint=h_blue,url_prefix='/house')
    # 初始化各种第三方库
    db.init_app(app)

    return app
