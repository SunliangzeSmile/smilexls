#!/usr/bin/env python3
#-*-coding:utf-8-*-
# /* * 
# @Author: sunliangzesmile 
#   @Date: 2019-09-28 18:28:16
#   @Last Modified by:   sunliangzesmile
#  @Last Modified time: 2019-09-28 18:28:16 
#  @Description:  
#* */

from config import app_config
from flask import Flask,request,url_for
from flask_wtf import CSRFProtect

from .views.home import home
from .views.blog import blog

app=Flask(__name__)
app.config.from_mapping(app_config)
app.register_blueprint(home)
app.register_blueprint(blog)
CSRFProtect(app)
