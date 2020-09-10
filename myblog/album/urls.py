# -*- coding: utf-8 -*-
"""图片墙路由
时间: 2020/9/8 15:36

作者: nola

更改记录:

重要说明:
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<int:page>.html', album, name='album'),  # 图片墙
]
