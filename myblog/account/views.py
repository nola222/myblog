from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

# Create your views here.


def register(request):
    """注册

    Args:
        request(object): Request对象

    Returns:

    """
    title = '注册博客'
    page_title = '用户注册'
    confirm_password = True
    button = '注册'
    url_text = '用户登录'
    url_name = 'user_login'

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('cp', '')
        if MyUser.objects.filter(username=username):
            tips = '用户已存在'
        elif confirm_password != password:
            tips = '两次输入的密码不一致'
        else:
            data = {
                'username': username,
                'password': password,
                'is_superuser': 1,  # 管理员身份
                'is_staff': 1  # 激活用户状态
            }
            user = MyUser.objects.create_user(**data)
            user.save()
            tips = '注册成功，请登录'
            logout(request)
            return redirect(reverse('user_login'))

    return render(request, 'user.html', locals())


def user_login(request):
    """登录
    """
    title = '登录博客'
    page_title = '用户登录'
    button = '登录'
    url_text = '用户注册'
    url_name = 'register'

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if MyUser.objects.filter(username=username):
            user = authenticate(username=username, password=password)  # 对用户进行认证，返回user object
            if user:
                if user.is_active:
                    login(request, user)
                    kwargs = {'id': request.user.id, 'page': 1}
                    return redirect(reverse('article', kwargs=kwargs))
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    else:
        if request.user.username:
            kwargs = {'id': request.user.id, 'page': 1}
            return redirect(reverse('article', kwargs=kwargs))
    return render(request, 'user.html', locals())
