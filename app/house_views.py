import os

from flask import Blueprint, render_template, request, jsonify, session

from app.models import User, House, Facility, HouseImage
from utils.setting import MEDIA_PATH

h_blue = Blueprint('house', __name__)


# 我的房源
@h_blue.route('/my_house/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')


@h_blue.route('/m_house/', methods=['GET', 'POST'])
def m_house():

    user = User.query.get(session.get('user_id'))
    name = user.id_name
    return jsonify({'code': 200, 'msg': '请求成功', 'name': name})


# 发布新房源
@h_blue.route('/new_house/', methods=['GET'])
def new_house():
    return render_template('newhouse.html')


# 我的房源展示
@h_blue.route('/house_info/', methods=['GET'])
def house_info():
    houses = House.query.filter(House.user_id == session.get('user_id')).all()
    show_house = [house.to_dict() for house in houses]
    return jsonify({'code': 200, 'houses': show_house})


@h_blue.route('/x_house/', methods=['POST'])
def x_house():
    # 获取数据
    title = request.form.get('title')
    price = request.form.get('price')
    area_id = request.form.get('area_id')
    addres = request.form.get('addres')
    room_count = request.form.get('room_count')
    acreage = request.form.get('acreage')
    unit = request.form.get('unit')
    capacity = request.form.get('capacity')
    beds = request.form.get('beds')
    deposit = request.form.get('deposit')
    min_days = request.form.get('min_days')
    max_days = request.form.get('max_days')
    facilities_f = request.form.getlist('facility')
    # 保存数据
    user_id = session.get('user_id')
    house = House()
    house.user_id = user_id
    house.title = title
    house.price = price
    house.area_id = area_id
    house.address = addres
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days

    for facility_id in facilities_f:
        facility = Facility.query.get(facility_id)
        # 多对多关联
        house.facilities.append(facility)
    house.add_update()
    session['house_id'] = house.id
    return jsonify({'code': 200})



@h_blue.route('/h_img/', methods=['POST'])
def h_img():
    house_id = session.get('house_id')
    img = request.files.get('house_image')
    path = os.path.join(MEDIA_PATH, img.filename)
    img.save(path)
    # house_id = request.form.get('house_id')
    house = House.query.get(house_id)
    # house = House()
    house.index_image_url = img.filename
    house.add_update()
    return jsonify({'code': 200})


@h_blue.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')\


@h_blue.route('/detail/<int:id>/', methods=['GET'])
def detail1(id):
    house = House.query.filter(House.id == id).first()
    house_image = HouseImage.query.filter(HouseImage.house_id == id).all()
    image = house.index_image_url
    images = []
    images.append(image)
    for i in house_image:
        images.append(i.url)
    data = {
        'code': 200,
        'house': house.to_full_dict(),
        'images': images
    }
    return jsonify(data)


@h_blue.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


@h_blue.route('/booking/<int:id>/', methods=['GET'])
def booking1(id):
    house = House.query.filter(House.id == id).first()
    data = {
        'code': 200,
        'house': house.to_dict()
    }
    return jsonify(data)



