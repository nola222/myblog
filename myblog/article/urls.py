# -*- coding: utf-8 -*-
"""博客文章路由
时间: 2020/9/8 15:36

作者: nola

更改记录:

重要说明:
"""
from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('', RedirectView.as_view(url='user/login.html')),  # 首页自动跳转到登录页
    path('<int:id>/<int:page>.html', article, name='article'),  # 文章列表
    path('detail/<int:id>/<int:aId>.html', detail, name='detail'),  # 文章详情

]
