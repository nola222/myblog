from django.db import models
from account.models import MyUser
from django.utils import timezone

# Create your models here.


class Board(models.Model):
    """留言板信息模型
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('留言用户', max_length=50, help_text='留言用户')
    email = models.CharField('邮箱地址', max_length=50, help_text='邮箱地址')
    content = models.CharField('留言内容', max_length=500, help_text='留言内容')
    created = models.DateTimeField('创建时间', default=timezone.now, help_text='创建时间')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        """设置返回值
        """
        return self.name

    class Meta:
        """留言板信息Meta类
        """
        verbose_name = '博客留言'
        verbose_name_plural = verbose_name

