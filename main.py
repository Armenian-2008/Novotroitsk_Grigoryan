from flask import Flask
import datetime
import sqlalchemy
from sqlalchemy import orm
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = "21"
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user2 = User()
    user2.surname = "Maykl"
    user2.name = "Pirson"
    user2.age = "20"
    user2.position = "colonist"
    user2.speciality = "engineer"
    user2.address = "module_2"
    user2.email = "maykl_pirson@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user2)
    db_sess.commit()
    user3 = User()
    user3.surname = "Peter"
    user3.name = "Parker"
    user3.age = "18"
    user3.position = "colonist"
    user3.speciality = "spider-man"
    user3.address = "module_3"
    user3.email = "spider_man@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user3)
    db_sess.commit()
    user4 = User()
    user4.surname = "Jon"
    user4.name = "Hanks"
    user4.age = "28"
    user4.position = "colonist"
    user4.speciality = "cook"
    user4.address = "module_4"
    user4.email = "jon_cooker@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user4)
    db_sess.commit()
    app.run()