# -*- coding: utf-8 -*-
"""用户路由
时间: 2020/9/8 15:35

作者: nola

更改记录:

重要说明:
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('register.html', register, name='register'),  # 用户注册
    path('login.html', user_login, name='user_login'),  # 用户登录
    path('about/<int:id>.html', about, name='about'),  # 关于我
]
