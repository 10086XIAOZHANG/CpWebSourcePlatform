# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 下午10:12
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : permissions.py
# @Software: PyCharm Community Edition
from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user