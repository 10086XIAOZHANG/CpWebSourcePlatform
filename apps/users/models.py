from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    """
       用户
       """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名",help_text="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月",help_text="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别",help_text="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话",help_text="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱",help_text="邮箱")
    avatar = models.ImageField(max_length=200, upload_to="avatar/images/", verbose_name="头像",help_text="头像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码",help_text="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话",help_text="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
