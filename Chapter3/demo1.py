# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo1.py

#@time: 2018/08/26

from flask import Flask,request,jsonify
from Chapter3.user import User
from Chapter3.ext import db
app = Flask(__name__)
app.config.from_object("Chapter3/configure2")
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/users',methods=["POST"])
def users():
    username = request.form.get("name")
    user = User(username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id':user.id})


if __name__ == "__main__":
    app.run(host="127.0.0.1",port="8080")



