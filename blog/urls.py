# -*- coding: utf-8 -*-
"""
@File        :  urls.py
@Modify Time :  2019/10/10 9:52      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  None
"""

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index),
    # 以下注释的两句，效果是一样的，即限制路径为空
    # 注意两句引用的包不一样，url可以识别正则
    # url(r'^$', views.index),
    # path('', views.index)
]
