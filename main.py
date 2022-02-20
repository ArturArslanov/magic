from datetime import datetime

from flask import Flask
from data import db_session
from config import secret_key, bd_path
from data.jobs import Jobs
from data.news import News
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
    user.hashed_password = "cap"
    session.add(user)
    session.commit()


    # app.run()


if __name__ == '__main__':
    main()
