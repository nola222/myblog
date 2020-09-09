from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    """自定义用户模型
    """
    name = models.CharField('姓名', max_length=50, default='匿名用户', help_text='姓名')
    introduce = models.TextField('简介', default='暂无介绍', help_text='简介')
    company = models.CharField('公司', max_length=100, default='暂无信息', help_text='公司')
    profession = models.CharField('职业', max_length=100, default='暂无信息', help_text='职业')
    address = models.CharField('住址', max_length=100, default='暂无信息', help_text='住址')
    telephone = models.CharField('电话', max_length=11, default='暂无信息', help_text='电话')
    wx = models.CharField('微信', max_length=50, default='暂无信息', help_text='微信')
    qq = models.CharField('QQ', max_length=50, default='暂无信息', help_text='QQ')
    wb = models.CharField('微博', max_length=100, default='暂无信息', help_text='微博')
    photo = models.ImageField('头像', blank=True, upload_to='images/user/', help_text='头像')

    def __str__(self):
        """设置返回值
        """
        return self.name
