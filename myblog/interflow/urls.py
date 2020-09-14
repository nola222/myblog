# -*- coding: utf-8 -*-
"""留言板路由
时间: 2020/9/8 15:37

作者: nola

更改记录:

重要说明:
"""
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/<int:page>.html', board, name='board'),  # 留言板
]
