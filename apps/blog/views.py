# Create your views here.
from .models import BlogActicle, BlogActicleBanner, BlogCategory
from .serializers import BlogActicleSerializers, BlogActicleBannerSerializers, BlogCategorySerializers,  \
    BlogActiclePublicSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .filters import BlogActicleFilter
from utils.permissions import IsOwnerOrReadOnly

class BlogActicleResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page_index'
    max_page_size = 100


class BlogActicleListViewSet(CacheResponseMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                             mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
     list:
    返回博客文章列表，过滤，排序，搜索，分页，以及根据ID返回某一篇文章
    """
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    queryset = BlogActicle.objects.all()
    serializer_class = BlogActicleSerializers
    pagination_class = BlogActicleResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filter_class = BlogActicleFilter
    search_fields = ('acticle_name', 'acticle_content')
    ordering_fields = ('comment_num', 'fav_num', 'click_num', 'add_time')

    # 动态设置serializer
    def get_serializer_class(self):
        if self.action == "create":
            return BlogActiclePublicSerializers
        return BlogActicleSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1  # 当用户获取某一条文章 表示点击数加一
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BlogActicleBannerListViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
     list:
    返回博客文章轮播图
    """
    queryset = BlogActicleBanner.objects.all()
    serializer_class = BlogActicleBannerSerializers


class BlogCategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
       返回博客文章类别
       """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    queryset = BlogCategory.objects.filter(category_type=1)
    serializer_class = BlogCategorySerializers
