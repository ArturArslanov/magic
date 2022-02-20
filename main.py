from datetime import datetime

from flask import Flask

from add_team import add_team, add_work
from data import db_session
from config import secret_key, bd_path
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


def main():
    db_session.global_init(bd_path)
    session = db_session.create_session()
    if not bool(session.query(User).all()):
        add_team(db_session)
    elif bool(session.query(User).all()) and not bool(session.query(Jobs).all()):
        add_work(db_session)
    else:
        app.run()


if __name__ == '__main__':
    main()
