# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 下午8:17
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : adminx.py
# @Software: PyCharm Community Edition

import xadmin
from .models import UserFav, UserLeavingMessage, UserComment, AppProfile


class UserFavAdmin(object):
    list_display = ['user', 'acticle', "add_time"]
    model_icon = 'fa fa-cogs'

class UserLeavingMessageAdmin(object):
    list_display = ['user', "message", "add_time"]
    model_icon = "fa fa-comments-o"

class UserCommentAdmin(object):
    list_display = ["user", "acticle", "comment_content", "add_time"]
    model_icon = "fa fa-comments"

class AppProfileAdmin(object):
    list_display = ["file", "add_time"]
    model_icon = "fa fa-app"

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserComment, UserCommentAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
xadmin.site.register(AppProfile, AppProfileAdmin)