#!/usr/bin/env python3
#-*-coding:utf-8-*-
# /* * 
# @Author: sunliangzesmile 
#   @Date: 2019-09-28 18:28:16
#   @Last Modified by:   sunliangzesmile
#  @Last Modified time: 2019-09-28 18:28:16 
#  @Description:  
#* */

from flask import session, request, redirect, abort, url_for, Blueprint
from ..tools.render import render_html

blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')
@render_html(template='blog/index.html')
def index():
    return {"page_title":u"Smile XLS"}