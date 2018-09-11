# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 下午8:43
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : serializers.py
# @Software: PyCharm Community Edition

from rest_framework import serializers
from .models import UserFav, UserLeavingMessage,UserComment
from blog.serializers import BlogActicleSerializers
from users.serializers import UserDetailSerializer

class UserFavDetailSerializer(serializers.ModelSerializer):
    acticle = BlogActicleSerializers()

    class Meta:
        model = UserFav
        fields = ("acticle", "id")


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ("user", "acticle", "id")


class UserLeavingMessageDetailSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    user = UserDetailSerializer()

    class Meta:
        model = UserLeavingMessage
        fields = ('user', 'message', 'subject', 'file', 'add_time', 'id')

class UserLeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    file = serializers.FileField(required=False)

    class Meta:
        model = UserLeavingMessage
        fields = ('user', 'message', 'subject', 'file', 'add_time', 'id')

class UserCommentDetailSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    user = UserDetailSerializer()
    acticle = BlogActicleSerializers()
    class Meta:
        model = UserComment
        fields = ('user', 'acticle', 'comment_content', 'file', 'add_time', 'id')

class UserCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    file = serializers.FileField(required=False)
    class Meta:
        model = UserComment
        fields = ('user', 'acticle', 'comment_content', 'file', 'add_time', 'id')
