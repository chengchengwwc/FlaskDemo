# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo3.py

#@time: 2018/08/

from flask import Flask,request,abort,redirect,url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/people/')
def people():
    print (request.args)
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return '{}-{}'.format(name,user_agent)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return user_id
    else:
        print ("DDD")
        return 'OPen login page'


@app.route('/secret/')
def secret():
    print ("AAAA")
    abort(404)
    print ("DDD")


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000')



