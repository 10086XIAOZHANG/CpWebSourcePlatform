from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserFav, UserLeavingMessage,UserComment
from .serializers import UserFavSerializer, UserFavDetailSerializer, UserLeavingMessageSerializer, \
    UserLeavingMessageDetailSerializer, UserCommentDetailSerializer,UserCommentSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    '''
      用户文章收藏 根据acticle_id查找 返回当前用户的收藏 以及收藏/取消收藏
    '''
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)

    lookup_field = "acticle_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        acticle = instance.acticle
        acticle.fav_num += 1  # acticle 收藏 收藏数加1
        acticle.save()

    def perform_destroy(self, instance):
        acticle = instance.acticle
        acticle.fav_num -= 1  # acticle 取消收藏 收藏数减1
        acticle.save()
        instance.delete()
        # 动态设置serializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        elif self.action == "list":
            return UserFavDetailSerializer
        return UserFavSerializer


class UserLeavingMessageViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    '''
    list:
        获取用户留言列表
    create:
        添加留言
    delect:
        删除留言
    '''
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('add_time',)

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserLeavingMessageDetailSerializer
        elif self.action == "create":
            return UserLeavingMessageSerializer
        return UserLeavingMessageSerializer


class UserCommentViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    '''
    list:
        获取用户评论列表
    create:
        添加评论
    delect:
        删除评论
    '''
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('add_time',)

    def get_queryset(self):
        return UserComment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserCommentDetailSerializer
        elif self.action == "create":
            return UserCommentSerializer
        return UserCommentSerializer
