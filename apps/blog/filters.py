# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 下午9:05
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : filters.py
# @Software: PyCharm Community Edition
import django_filters
from django_filters import rest_framework as filters
from .models import BlogActicle


class BlogActicleFilter(filters.FilterSet):
    acticle_name = django_filters.CharFilter(name='acticle_name', lookup_expr='icontains', help_text="文章名")
    acticle_content = django_filters.CharFilter(name='acticle_content', lookup_expr='icontains', help_text="文章内容")

    class Meta:
        model = BlogActicle
        fields = ('acticle_name', 'acticle_content')
