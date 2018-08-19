# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo6.py

#@time: 2018/08/19

from flask import Flask,jsonify
from flask.views import MethodView

app = Flask(__name__)





class UserAPI(MethodView):

    def get(self):
        return jsonify({
            'user_name':'fake',
            'age':18
        })

    def post(self):
        return 'UNSUPPORTED'


app.add_url_rule('/user/',view_func=UserAPI.as_view('userapi'))






