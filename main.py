from datetime import datetime

from flask import Flask, render_template

from add_team import add_team, add_work
from data import db_session
from config import secret_key, bd_path, params
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


def main():
    db_session.global_init(bd_path)
    session = db_session.create_session()
    if not bool(session.query(User).all()):
        add_team(db_session)
    if not bool(session.query(Jobs).all()):
        add_work(db_session)
    app.run(port=8081, host='127.0.0.2')


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', **params,jobs=jobs)


if __name__ == '__main__':
    main()
