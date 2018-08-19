# -*- coding: utf-8 -*-

#@author: weicheng

#@file: user.py

#@time: 2018/08/19

from flask import Blueprint

bp = Blueprint('user',__name__,url_prefix='/user/')


@bp.route('/')
def index():
    return "Hello World"



