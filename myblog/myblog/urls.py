"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),  # 用户注册和登录
    path('', include('article.urls')),  # 博客文章
    path('album/', include('album.urls')),  # 照片墙
    path('board/', include('interflow.urls')),  # 留言板
    re_path('media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT}, name='media'),  # 配置媒体资源
]
