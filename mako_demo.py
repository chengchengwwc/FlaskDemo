# -*- coding: utf-8 -*-

#@author: weicheng

#@file: mako_demo.py

#@time: 2018/08/19


from mako.template import Template

template = Template('Hello ${name}!')
template.render(name='World')

