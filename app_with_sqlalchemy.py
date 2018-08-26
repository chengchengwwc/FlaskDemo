# -*- coding: utf-8 -*-

#@author: weicheng

#@file: app_with_sqlalchemy.py

#@time: 2018/08/26

import random
from flask import Flask,g,render_template
from Chapter3.ext import db
from Chapter3.user import User

app = Flask(__name__,template_folder="template")
app.config.from_object("config")
db.init_app(app)

def get_current_user():
    users = User.query.all()
    return random.choice(users)

@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()
    fake_users = [
        User("xiaoming","ddd"),
        User("xiaolele","SSDS"),
        User("xiaowenwen",'sfsf')
    ]
    db.session.add_all(fake_users)
    db.session.commit()


@app.before_request
def before_request():
    g.user = get_current_user()


@app.teardown_appcontext
def teardown(exc=None):
    if exc is None:
        db.session.commit()
    else:
        db.session.rollback()
    db.session.remove()
    g.user =None



@app.context_processor
def template_extras():
    return {"enumerate":enumerate,'current_user':g.user}


@app.errorhandler(404)
def page_not_found(error):
    return 'This Page is not found'


@app.template_filter('capitalize')
def reverse_filter(s):
    return s.capitalize()



def user_view():
    users = User.query.all()
    return render_template('user.html',users=users)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)















