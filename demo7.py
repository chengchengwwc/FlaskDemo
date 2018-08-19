# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo7.py

#@time: 2018/08/19

from flask import Flask,g

app = Flask(__name__)

app.config['SERVER_NAME'] = 'example.com:8000'

@app.url_value_preprocessor
def get_site(endpoint,values):
    g.site = values.pop('subdomain')

@app.route('/',subdomain='<subdomain>')
def index():
    return g.site

