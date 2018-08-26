# -*- coding: utf-8 -*-

#@author: weicheng

#@file: mako_demo2.py

#@time: 2018/08/19

from mako.lookup import TemplateLookup
from mako.template import Template

myloop = TemplateLookup(directories=['template/flaskdemo'])
template = Template('<%include file="hello.mako"/>',lookup=myloop)
template.render(name='WORLD')
