from django.db import models
from account.models import MyUser
from django.utils import timezone

# Create your models here.


class ArticleTag(models.Model):
    """文章分类标签模型
    """
    id = models.AutoField(primary_key=True)
    tag = models.CharField('标签', max_length=500, help_text='标签')
    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        """设置返回值
        """
        return self.tag

    class Meta:
        """文章分类标签Meta
        """
        verbose_name = '博文分类'
        verbose_name_plural = verbose_name


class ArticleInfo(models.Model):
    """文章信息模型
    """
    author = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField('标题', max_length=200, help_text='标题')
    content = models.TextField('内容', help_text='内容')
    article_photo = models.ImageField('文章图片', blank=True, upload_to='images/article/')
    reading = models.IntegerField('阅读量', default=0, help_text='阅读量')
    liking = models.IntegerField('点赞量', default=0, help_text='点赞量')
    created = models.DateTimeField('创建时间', default=timezone.now, help_text='创建时间')
    updated = models.DateTimeField('更新时间', auto_now=True, help_text='更新时间')
    article_tag = models.ManyToManyField(to=ArticleTag, blank=True, verbose_name='文章标签')

    def __str__(self):
        """设置返回值
        """
        return self.title

    class Meta:
        """文章信息Meta类
        """
        verbose_name = '博文管理'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """评论信息模型
    """
    article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE, verbose_name='所属文章')
    commentator = models.CharField('评论用户', max_length=90, help_text='评论用户')
    content = models.TextField('评论内容', help_text='评论内容')
    created = models.DateTimeField('创建时间', auto_now_add=True, help_text='评论时间')

    def __str__(self):
        """设置返回值
        """
        return self.article.title

    class Meta:
        """评论信息Meta类
        """
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name
