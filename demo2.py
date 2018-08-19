# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo2.py

#@time: 2018/08/19

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/abc/1/')
def item(id):
    pass


with app.test_request_context():
    print (url_for('item',id='1'))
    print (url_for('item',abc='d'))







