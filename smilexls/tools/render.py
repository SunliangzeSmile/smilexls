#!/usr/bin/env python3
#-*-coding:utf-8-*-
# /* *
#   @Author: sunliangzesmile
#   @Date: 2019-09-28 18:28:16
#   @Last Modified by:   sunliangzesmile
#  @Last Modified time: 2019-09-28 18:28:16
#  @Description:
#* */
from flask import render_template


def render_html(template):
    """
    html模板渲染修时器
    """
    def render(func):
        def wrapper(*arg, **kw):
            context = func(*arg, **kw)
            return render_template(template, **context)
        return wrapper
    return render