# -*- coding: utf-8 -*-

#@author: weicheng

#@file: app_bp.py

#@time: 2018/08/19


from flask import Flask
import user

app = Flask(__name__)
app.register_blueprint(user.bp)

if __name__ == "__main__":
    app.run('127.0.0.1',8000)
