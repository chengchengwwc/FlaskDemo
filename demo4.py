# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo4.py

#@time: 2018/08/19

from flask import Flask,jsonify
from werkzeug.wrappers import Response


app = Flask(__name__)


class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response,dict):
            response = jsonify(response)
        return super(JSONResponse,cls).force_type(response,environ)

app.response_class = JSONResponse

@app.route('/')
def hello_world():
    return {'message':'Hello World'}


@app.route('/custom_headers/')
def headers():
    return {'headers':[1,2,3]},201,[('X-Request-Id','100')]


if __name__ == "__main__":
    app.run('127.0.0.1','8000')














