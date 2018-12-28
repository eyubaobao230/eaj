import os
import random
import re

from flask import Blueprint, request, render_template, jsonify, session

from app.models import User
from utils import status_code
from utils.functions import is_login
from utils.setting import MEDIA_PATH

u_blue = Blueprint('user', __name__)


# 注册
@u_blue.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        mobile = request.form.get('mobile')
        imagecode = request.form.get('imagecode')
        # phonecode = request.form.get('phonecode')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 判断各输入框是否完全输入
        if not all([mobile, imagecode, password]):
            return jsonify(status_code.USER_LOGIN_IS_INVALID)
        #判断手机号码是否正确
        phone = r'^(1(2|3|7|8|9|6|5|4)|1(0|8|3|7)|1(2|3|6|7|9)|1(2|3|4|5|6|7|8|9))\d{9}$'
        if not re.match(phone, mobile):
            return jsonify({'code': 1001, 'msg': '请输入正确的手机号码'})

        if password != password2:
            return jsonify({'code': 1002, 'msg': '两次密码不一致'})

        i_code = session.get('i_code')
        if imagecode != i_code:
            return jsonify({'code':1003, 'msg': '验证码不正确'})

        user = User()
        user.phone = mobile
        user.password = password
        user.add_update()
        return jsonify({'code': 200, 'msg': '请求成功'})


# 图片验证
@u_blue.route('/img_code/', methods = ['GET'])
def img_code():
    codes = '1234567890qwertyuiopasdfgjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    img_code = ''
    for i in range(2):
        code = random.choice(codes)
        img_code += code
    session['i_code'] = img_code
    return jsonify({'code':200, 'data':img_code})


# 首页
@u_blue.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        pass


# 登录
@u_blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        # 检验填写的完整性
        if not all([mobile, password]):
            return jsonify({'code': 1001, 'msg': '请输入正确手机号或密码'})
        # 判断手机号是否已注册
        user = User.query.filter(User.phone == mobile).first()
        if not user:
            return jsonify({'code': 1002, 'msg': '手机号未注册，请注册'})
        # 判断密码是否与数据库密码相同
        if not user.check_pwd(password):
            return jsonify({'code': 1003, 'msg': '密码错误'})
        session['user_id'] = user.id
        return jsonify({'code': 200, 'msg': '请求成功'})


# 个人中心
@u_blue.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')


# 信息
@u_blue.route('/get_user/', methods=['GET'])
def get_user():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    username = user.name
    phone = user.phone
    avat = user.avatar
    return jsonify({'code':200, 'username': username, 'phone':phone, 'avat':avat})


# 登录后首页
@u_blue.route('/user_info/', methods=['GET'])
def user_info():
    # 拿到session中的当前登录用户的id
    user_id = session.get('user_id')
    # 通过用户的id去数据库中拿到用户信息
    user = User.query.get(user_id)
    # 从数据库中拿到用户的名字（用户名）
    username = user.name
    # 成功后返回200状态码，并将数据返回给前端
    return jsonify({'code': 200, 'msg': '已登录', 'user': user_id, 'username': username})



# 个人信息
@u_blue.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')

# 上传头像
@u_blue.route('/up_avatar/', methods=['PATCH'])
def up_avatar():
    # 使用files获取文件，前端没有返回页面，可以直接在后台写上想要获取的标签名称，即name
    img = request.files.get('avatar')
    path = os.path.join(MEDIA_PATH, img.filename)
    img.save(path)
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    user.avatar = img.filename
    user.add_update()
    return jsonify({'code': 200, 'msg': '上传成功', 'avatar': img.filename})




# 上传用户名
@u_blue.route('/up_username/', methods=['PATCH'])
def up_username():
    username = request.form.get('username')
    user_id = session.get('user_id')
    u_name = User.query.filter(User.name == username).first()
    if u_name:
        return jsonify({'code': 2001, 'msg': '该用户名已存在'})
    user = User.query.get(user_id)
    user.name = username
    user.add_update()
    return jsonify({'code': 200, 'msg': '保存成功'})


@u_blue.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


# 实名认证
@u_blue.route('/my_auth/', methods=['GET'])
def my_auth():
    real_name = request.args.get('real_name')
    id_card = request.args.get('id_card')
    if not all(['real_name', 'id_card']):
        return jsonify({'code': 3001, 'msg': '请输入完整信息'})

    user_id = session.get('user_id')
    user = User.query.get(user_id)
    user.id_name = real_name
    user.id_card = id_card
    user.add_update()
    return jsonify({'code': 200, 'msg': '保存成功'})





