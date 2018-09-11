# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 下午6:42
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : signals.py
# @Software: PyCharm Community Edition

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
