from datetime import datetime

from flask import Flask

from add_team import add_team
from data import db_session
from config import secret_key, bd_path
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


def main():
    db_session.global_init(bd_path)
    add_team(db_session)

    # app.run()


if __name__ == '__main__':
    main()
