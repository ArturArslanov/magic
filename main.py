from datetime import datetime

from flask import Flask
from data import db_session
from config import secret_key, bd_path
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


def main():
    db_session.global_init(bd_path)
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password("cap")
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Marli"
    user.name = "Rayner"
    user.age = 25
    user.position = "colonist"
    user.speciality = "dragon pilot"
    user.address = "module_3"
    user.email = "Rayner_ray@mars.org"
    user.set_password("i`m_armored")
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Holmes"
    user.name = "Sherlock"
    user.age = 25
    user.position = "colonist"
    user.speciality = "detective consultant"
    user.address = "module_2"
    user.email = "Sheri_shegi@mars.org"
    user.set_password('I`m_sherlocked')
    session.add(user)
    session.commit()

    session = db_session.create_session()
    user = User()
    user.surname = "Watson"
    user.name = "John"
    user.age = 28
    user.position = "colonist"
    user.speciality = "doctor"
    user.address = "module_4"
    user.email = "John_John@mars.org"
    user.set_password('i_Love_Mary_Morstan')
    session.add(user)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
