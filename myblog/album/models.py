from django.db import models
from account.models import MyUser

# Create your models here.


class AlbumInfo(models.Model):
    """照片墙信息模型
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField('标题', max_length=50, blank=True, help_text='标题')
    introduce = models.CharField('描述', max_length=200, blank=True, help_text='描述')
    photo = models.ImageField('图片', blank=True, upload_to='images/album/', help_text='图片')

    def __str__(self):
        """设置返回值
        """
        return str(self.id)

    class Meta:
        """照片墙信息Meta类
        """
        verbose_name = '图片墙管理'
        verbose_name_plural = verbose_name
