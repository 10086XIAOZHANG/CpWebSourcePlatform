from datetime import datetime
from django.db import models
from users.models import UserProfile as User
from blog.models import BlogActicle


# Create your models here.
class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    acticle = models.ForeignKey(BlogActicle, verbose_name="文章", help_text="文章id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "acticle")

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    user = models.ForeignKey(User, verbose_name="发起者", on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default="", verbose_name="主题", help_text="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(upload_to="message/files/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserComment(models.Model):
    """
    用户评论
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    acticle = models.ForeignKey(BlogActicle, verbose_name="文章", help_text="文章id", on_delete=models.CASCADE)
    comment_content = models.TextField(default="", verbose_name="评论内容", help_text="评论内容")
    file = models.FileField(upload_to="message/files/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name
        unique_together = ("user", "acticle")

    def __str__(self):
        return self.user.username


class AppProfile(models.Model):
    '''
        app 信息
    '''
    file = models.FileField(upload_to="message/files/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = 'app 信息'
        verbose_name_plural = verbose_name
