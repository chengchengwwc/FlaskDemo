# -*- coding: utf-8 -*-

#@author: weicheng

#@file: user.py

#@time: 2018/08/26

from Chapter3.ext import db

class User(db.Model):
    __tablename__ = "users2"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    email_address = db.Column(db.String(128), nullable=True)

    def __init__(self,name,email):
        self.name = name
        self.email_address = email


