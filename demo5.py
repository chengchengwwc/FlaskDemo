# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo5.py

#@time: 2018/08/19


from flask import Flask,request,render_template
from flask.views import View

app = Flask(__name__,template_folder='template')


class BaseView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self,content):
        return render_template(self.get_template_name(),**content)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED'
        context = {"users":self.get_users()}
        print (context)
        return self.render_template(context)


class UserView(BaseView):

    def get_template_name(self):
        return 'users.html'

    def get_users(self):
        return [{
            'user_name':'fake',
            'avatar':"https://www.baidu.com"
        }]


app.add_url_rule('/users/',view_func=UserView.as_view('userview'))

if __name__ == "__main__":
    app.run('127.0.0.1', '8000')




















