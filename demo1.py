# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo1.py

#@time: 2018/08/19

from flask import Flask
import urllib
from werkzeug.routing import BaseConverter

app = Flask(__name__)

app.config['DEBUG'] = True


class ListConvert(BaseConverter):

    def __init__(self,url_map,separator):
        super(ListConvert,self).__init__(url_map)
        self.separator = urllib.unquote(separator)

    def to_python(self,value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(super(ListConvert,self).to_url(value) for value in values)


app.url_map.converters['list'] = ListConvert







@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
